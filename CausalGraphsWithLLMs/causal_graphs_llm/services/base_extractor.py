from abc import ABC, abstractmethod

from causal_graphs_llm.services.config import ExtractorConfig


class BaseExtractor(ABC):
    """
    Handles all interaction with the LLM for extracting variables and relations from text.
    """

    def __init__(self, config: ExtractorConfig):
        pass

    @abstractmethod
    def query(self, prompt):
        pass

    @abstractmethod
    def extract_variables(self, prompt):
        pass
