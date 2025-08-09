# Causal-Graphs-With-LLMs

Causal-Graphs-With-LLMs is a Python project for constructing, evaluating, and visualizing causal graphs using Large Language Models (LLMs). It provides a modular pipeline for graph building, prompt-based extraction, and evaluation against ground truth datasets.

## Project Structure

```
CausalGraphsWithLLMs/
├── __init__.py                         # Marks root package
├── poetry.lock                         # Poetry lock file for exact dependency versions
├── pyproject.toml                       # Project metadata & dependencies
└── causal_graphs_llm/
    ├── __init__.py                     # Marks main package
    ├── core/                           # Core pipeline logic
    │   ├── pipeline.py                 # Orchestrates initialization → expansion → insertion stages
    │   └── stages/                     # Stage-specific procedures
    │       ├── expansion.py            # Finds variables caused by the current variable
    │       ├── initialization.py       # Finds variables with no causes (BFS queue start)
    │       └── insertion.py            # Adds edges without creating cycles
    ├── evaluation/                     # Evaluation & visualization tools
    │   ├── evaluator.py                # Compares predicted vs ground truth graphs
    │   ├── visualizer.py               # Graph plotting & diagram generation
    │   └── ground_truth_graphs/        # Benchmark datasets for testing
    │       ├── asia                    # Asia dataset
    │       ├── child                   # Child dataset
    │       └── neuropathic             # Neuropathic pain dataset
    ├── graphs/                         # Graph construction logic
    │   └── builder.py                  # Builds causal graph data structures
    ├── models/                         # Data models (Pydantic, domain objects)
    │   └── causal.py                   # Node, Edge, Graph model definitions
    ├── prompts/                        # Prompt engineering for LLM queries
    │   ├── __init__.py
    │   ├── extraction_prompt.py        # Prompts for variable relationship extraction
    │   └── initialization_prompt.py    # Prompts for identifying initial variables
    └── services/                       # LLM interaction layer
        ├── base_extractor.py           # Abstract base class for extractors
        ├── config.py                   # Service configuration (model, API keys, etc.)
        └── extractor.py                # Implementation of LLM query & response parsing
```

## Main Components
- **core/pipeline.py**: Orchestrates the causal graph construction pipeline.
- **core/stages/**: Contains modules for different pipeline stages (expansion, initialization, insertion).
- **evaluation/**: Tools for evaluating and visualizing generated graphs, with ground truth datasets.
- **graphs/builder.py**: Utilities for building graph structures.
- **models/causal.py**: Causal graph model definitions.
- **prompts/**: Prompt templates for LLM-based extraction and initialization.
- **services/**: Service classes for extraction and configuration.

## Getting Started
1. Install Poetry (if not already installed):
   ```bash
   pip install poetry
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Run the pipeline or evaluation scripts as needed.


## References

- **Can Large Language Models Build Causal Graphs?**: This paper shows that LLMs like GPT-3 can assist in building causal graphs, but expert verification is still necessary due to possible errors and omissions. [Read the paper](https://arxiv.org/pdf/2303.05279)

- **Efficient Causal Graph Discovery Using Large Language Models**: This work introduces a breadth-first search method with LLMs for efficient causal graph discovery, achieving state-of-the-art results without requiring observational data. [Read the paper](https://arxiv.org/pdf/2402.01207)





