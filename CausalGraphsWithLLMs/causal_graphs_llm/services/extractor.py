from causal_graphs_llm.services.base_extractor import BaseExtractor
from causal_graphs_llm.services.config import ExtractorConfig


class OpenaiExtractor(BaseExtractor):
    """
    Handles all interaction with the LLM for extracting variables and relations from text.
    """

    def __init__(self, config: ExtractorConfig):
        pass
