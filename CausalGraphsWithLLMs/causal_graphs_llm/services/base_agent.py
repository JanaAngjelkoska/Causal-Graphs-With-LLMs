"""
Handles all interaction with an LLM for extracting variables and relations from text.
"""
from abc import ABC, abstractmethod
from typing import List

from causal_graphs_llm.services.config import ExtractorConfig


class BaseAgent(ABC):

    def __init__(self, config: ExtractorConfig):
        self.config = config

    @abstractmethod
    def initialization_query(self, prompt):
        """
        Given a prompt, query the LLM and return structured output used in the initialization stage.
        """
        pass

    @abstractmethod
    def extraction_query(self, cause: str, effect: List[str]):
        """
        Given a prompt, query the LLM and return structured output in the extraction stage.
        """
        pass

    @abstractmethod
    def _query_llm(self, prompt: str) -> str:
        """
        Send the prompt to the LLM and return raw string output.
        Must be implemented by each concrete LLM extractor.
        """
        pass
