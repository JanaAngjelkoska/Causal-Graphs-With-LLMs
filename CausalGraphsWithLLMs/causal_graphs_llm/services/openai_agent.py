import os
import openai
from json import JSONDecodeError
from dotenv import load_dotenv
load_dotenv()
from causal_graphs_llm.prompts.extraction_prompt import create_extraction_prompt
from causal_graphs_llm.prompts.initialization_prompt import create_initialization_prompt
from causal_graphs_llm.models.causal import InitializationResponse, ExpansionResponse
from causal_graphs_llm.services.base_agent import BaseAgent
from causal_graphs_llm.services.config import ExtractorConfig


class OpenAIAgent(BaseAgent):
    def __init__(self, config: ExtractorConfig):
        super().__init__(config)
        openai.api_key = config.api_key or os.getenv("OPENAI_API_KEY")
        if config.api_base:
            openai.api_base = config.api_base

    def _query_llm(self, prompt: str) -> str:
        response = openai.chat.completions.create(
            model=self.config.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens,
        )
        return response.choices[0].message["content"].strip()

    def initialization_query(self, prompt: str) -> InitializationResponse:
        refined_prompt = create_initialization_prompt(prompt)
        raw_output = self._query_llm(refined_prompt)
        try:
            return InitializationResponse.model_validate_json(raw_output)
        except JSONDecodeError:
            raise ValueError(f"LLM returned invalid JSON for initialization: {raw_output}")

    def extraction_query(self, prompt: str) -> ExpansionResponse:
        refined_prompt = create_extraction_prompt(prompt)
        raw_output = self._query_llm(refined_prompt)
        try:
            return ExpansionResponse.model_validate_json(raw_output)
        except JSONDecodeError:
            raise ValueError(f"LLM returned invalid JSON for extraction: {raw_output}")

if __name__ == "__main__":

    config = ExtractorConfig()
    print("Using OpenAI Extractor with model:", config.model)
    agent = OpenAIAgent(config)
    print("Initialized OpenAI Extractor")
    response = agent.query_llm("Hello, how are you?")
    print(response)