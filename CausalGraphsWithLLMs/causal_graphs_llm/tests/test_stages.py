from unittest.mock import MagicMock
from collections import deque

from causal_graphs_llm.services.openai_agent import GitHubLLMAgent
from causal_graphs_llm.models.causal import InitializationResponse, ExpansionResponse
from causal_graphs_llm.core.pipeline import Pipeline
from causal_graphs_llm.core.stages.initialization import initialization_stage
from causal_graphs_llm.core.stages.expansion import expansion_stage


def test_initialization_stage_classifies_vars():
    vars_dict = {
        "A": "INDEPENDENT",
        "B": "DEPENDENT",
        "C": "INDEPENDENT"
    }
    independent, dependent = initialization_stage(vars_dict)
    assert set(independent) == {"A", "C"}
    assert set(dependent) == {"B"}


def test_expansion_stage_updates_queue():
    visited = deque(["A"])
    effects = ["B", "C"]
    updated_queue = expansion_stage("A", effects, visited)
    assert list(updated_queue) == ["B", "C"]


def test_pipeline_builds_graph_without_cycles():
    # Mock agent
    mock_agent = MagicMock(spec=GitHubLLMAgent)

    mock_agent.initialization_query.return_value = InitializationResponse(
        root_variables={"X": "INDEPENDENT", "Y": "DEPENDENT"}
    )

    # Mock extraction response
    def extraction_side_effect(cause, effects):
        mapping = {
            "X": ExpansionResponse(variable="X", effects=["Y"]),
            "Y": ExpansionResponse(variable="Y", effects=["Z"]),
            "Z": ExpansionResponse(variable="Z", effects=[])
        }
        return mapping.get(cause, ExpansionResponse(variable=cause, effects=[]))

    mock_agent.extraction_query.side_effect = extraction_side_effect

    pipeline = Pipeline()
    graph = pipeline.run_pipeline(mock_agent, "query string")

    expected_graph = {
        "X": ["Y"],
        "Y": ["Z"],
        "Z": []
    }
    assert graph == expected_graph


