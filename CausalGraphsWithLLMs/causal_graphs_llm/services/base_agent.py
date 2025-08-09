from abc import ABC, abstractmethod
from causal_graphs_llm.services.config import ExtractorConfig


class BaseAgent(ABC):
    """
    Handles all interaction with an LLM for extracting variables and relations from text.
    """

    def __init__(self, config: ExtractorConfig):
        self.config = config

    @abstractmethod
    def initialization_query(self, prompt: str):
        pass

    @abstractmethod
    def extraction_query(self, prompt: str):
        pass

    @abstractmethod
    def _query_llm(self, prompt: str) -> str:
        """
        Send the prompt to the LLM and return raw string output.
        Must be implemented by each concrete LLM extractor.
        """
        pass
