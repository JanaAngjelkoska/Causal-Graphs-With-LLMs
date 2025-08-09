from typing import Tuple

from causal_graphs_llm.core.stages.expansion import expansion_stage
from causal_graphs_llm.core.stages.initialization import initialization_stage
from causal_graphs_llm.core.stages.insertion import insertion_stage
from causal_graphs_llm.graphs.builder import Builder

class Pipeline:
    def run_pipeline(self, variables: Tuple[str], edges: Tuple[str], ):
        """
        Runs the three pipeline stages in sequence, without building the graph here.
        The builder handles actual graph creation.
        """
        queue = initialization_stage(self, variables, edges)
        visited = set()
        cause, effects = expansion_stage(queue, edges, visited)
        insertion_stage(cause, effects, queue)

        builder = Builder()
        builder.build_from_edges(edges)

        return builder