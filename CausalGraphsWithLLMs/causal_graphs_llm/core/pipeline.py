from collections import deque
from typing import List, Dict

from causal_graphs_llm.core.stages.expansion import expansion_stage
from causal_graphs_llm.core.stages.initialization import initialization_stage
from causal_graphs_llm.services.base_agent import BaseAgent


class Pipeline:
    def run_pipeline(self, agent: BaseAgent, query: str) -> Dict[str, List[str]]:
        """
        Runs the three pipeline stages in sequence, building the graph incrementally
        and checking if it remains a DAG.

        Args:
            agent: BaseAgent instance for querying variables and effects
        Returns:
            Dict: The constructed causal graph {variable: [caused_variables]}
        """
        # initialization Stage
        root_variables = agent.initialization_query(query)
        independent_vars, dependent_vars = initialization_stage(root_variables.root_variables)

        graph = {}
        expanded = set()
        queue = deque()

        for var in independent_vars:
            if var not in graph:
                graph[var] = []
            queue.append(var)

        # expansion and insertion stages
        while queue:
            current_var = queue.popleft()
            if current_var in expanded:
                continue
            response = agent.extraction_query(current_var, dependent_vars)
            effects = response.effects
            expanded.add(current_var)
            for effect in effects:
                if effect not in graph:
                    graph[effect] = []
                if not self._has_cycle(graph, current_var, effect):
                    graph[current_var].append(effect)
                    if effect not in expanded and effect not in queue:
                        queue.append(effect)
                else:
                    print(f"Cycle detected: Cannot add edge {current_var} -> {effect}")

        return graph

    def _has_cycle(self, graph: Dict[str, List[str]], start_var: str, target_var: str) -> bool:
        """
        Helper method to detect if adding an edge from start_var to target_var creates a cycle.
        Uses DFS from target_var to see if start_var is reachable.
        """
        visited = set()

        def dfs(current_var: str) -> bool:
            if current_var == start_var:
                return True
            visited.add(current_var)
            for neighbor in graph.get(current_var, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(target_var)
