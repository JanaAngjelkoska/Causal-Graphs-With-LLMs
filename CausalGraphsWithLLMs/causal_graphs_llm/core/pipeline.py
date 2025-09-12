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
        Helper method to detect cycles using DFS.

        Args:
            graph: Dictionary representing the causal graph
            start_var: Starting variable
            target_var: Target variable to check for cycle
        Returns:
            bool: True if adding the edge creates a cycle, False otherwise
        """
        visited = set()
        rec_stack = set()

        def dfs(current_var: str) -> bool:
            visited.add(current_var)
            rec_stack.add(current_var)

            for neighbor in graph.get(current_var, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(current_var)
            return False

        if start_var not in graph:
            graph[start_var] = []
        graph[start_var].append(target_var)
        has_cycle = dfs(start_var)
        graph[start_var].remove(target_var)
        return has_cycle
