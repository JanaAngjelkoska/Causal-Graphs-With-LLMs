import logging
from causal_graphs_llm.core.pipeline import Pipeline
from causal_graphs_llm.graphs.builder import Builder
from causal_graphs_llm.services.config import ExtractorConfig
from causal_graphs_llm.services.openai_agent import GitHubLLMAgent

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)

if __name__ == '__main__':
    config = ExtractorConfig()
    logger.info("Loaded ExtractorConfig.")
    agent = GitHubLLMAgent(config=config)
    logger.info("Initialized OpenAILLMAgent.")
    graph = Pipeline().run_pipeline(agent=agent, query="After the heavy rainfall caused flooding in the city,"
                                                       " the power outage led to hospital generator failure, "
                                                       "which resulted in delayed patient treatments and increased mortality rates.")
    logger.info("Pipeline run complete. Building graph.")
    Builder().build_graph(graph=graph)
    logger.info("Graph building complete.")
