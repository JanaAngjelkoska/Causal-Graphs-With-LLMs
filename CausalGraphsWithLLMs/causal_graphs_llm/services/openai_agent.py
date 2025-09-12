"""
Handles all interaction with an LLM for extracting variables and relations from text,
using GitHub GPT-5 via Azure-style API with JSON output.
"""
import os
import json
import logging
from typing import List

try:
    import colorlog
    logger = colorlog.getLogger(__name__)
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(name)s:%(message)s',
        log_colors={
            'info()': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
    ))
    logging.basicConfig(level=logging.INFO, handlers=[handler])
except ImportError:
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

from causal_graphs_llm.services.base_agent import BaseAgent
from causal_graphs_llm.services.config import ExtractorConfig
from causal_graphs_llm.models.causal import InitializationResponse, ExpansionResponse
from causal_graphs_llm.prompts.extraction_prompt import create_extraction_prompt
from causal_graphs_llm.prompts.initialization_prompt import create_initialization_prompt
from causal_graphs_llm.services.helpers.json_parser import clean_llm_content, clean_llm_json

logger.info("Initializing GitHubLLMAgent...")


class GitHubLLMAgent(BaseAgent):
    def __init__(self, config: ExtractorConfig):
        super().__init__(config)

        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            raise ValueError("GITHUB_TOKEN environment variable not set.")
        else:
            logger.info("GITHUB_TOKEN found in environment variables.")

        self.client = ChatCompletionsClient(
            endpoint=config.endpoint,
            credential=AzureKeyCredential(token)
        )
        logger.info(f"Connected to LLM endpoint: {config.endpoint}")

        self.model = config.model
        self.max_tokens = config.max_tokens
        logger.info(f"Using model: {self.model}, max tokens: {self.max_tokens}")

    def _query_llm(self, prompt: str) -> str:
        logger.info("Sending query to GitHub GPT-5...")
        logger.info(f"Prompt:\n{prompt}")

        try:
            response = self.client.complete(
                messages=[
                    SystemMessage("You are a helpful AI assistant that outputs JSON."),
                    UserMessage(prompt)
                ],
                model=self.model
            )
        except Exception as e:
            logger.error(f"Error communicating with LLM: {str(e)}")
            raise

        content = response.choices[0].message.content
        logger.info(f"Raw LLM response content:\n{content}")

        if not content or not content.strip():
            logger.error("LLM response content is empty.")
            raise ValueError("LLM response content is empty.")

        cleaned = clean_llm_content(content)
        logger.info(f"Cleaned LLM JSON content:\n{cleaned}")

        # Try to parse cleaned content as JSON
        try:
            clean_llm_json(cleaned)
        except Exception as e:
            logger.error(f"Cleaned content is not valid JSON: {str(e)}\nContent: {cleaned}")
            raise

        return cleaned

    def initialization_query(self, prompt: str) -> InitializationResponse:
        """
        Sends the initialization prompt to the LLM and parses it into InitializationResponse.
        """
        logger.info("Running initialization query...")
        full_prompt = create_initialization_prompt(prompt)
        logger.info(f"Full initialization prompt:\n{full_prompt}")

        raw_response = self._query_llm(full_prompt)

        try:
            response_dict = clean_llm_json(raw_response)
            if 'root_variables' in response_dict:
                parsed = InitializationResponse.model_validate(response_dict)
            elif 'choices' in response_dict:
                content = response_dict["choices"][0]["message"]["content"]
                variables_dict = clean_llm_json(content)
                if "root_variables" not in variables_dict:
                    wrapped = {"root_variables": variables_dict}
                else:
                    wrapped = variables_dict
                parsed = InitializationResponse.model_validate(wrapped)
            else:
                parsed = InitializationResponse.model_validate({"root_variables": response_dict})
            logger.info("Initialization query parsed successfully.")
            return parsed
        except Exception as e:
            logger.error(f"Failed to parse initialization response: {str(e)}")
            raise

    def extraction_query(self, cause: str, effect: List[str]) -> ExpansionResponse:
        """
        Sends an extraction query for a cause variable and its dependent effects.
        """
        logger.info(f"Running extraction query for cause: {cause}")
        full_prompt = create_extraction_prompt(cause, effect)
        logger.info(f"Full extraction prompt:\n{full_prompt}")

        raw_response = self._query_llm(full_prompt)
        try:
            response_dict = clean_llm_json(raw_response)
            parsed = ExpansionResponse.model_validate(response_dict)
            logger.info(f"Extraction query parsed successfully for cause: {cause}")
            return parsed
        except Exception as e:
            logger.error(f"Failed to parse extraction response for cause {cause}: {str(e)}")
            raise
