# Causal-Graphs-With-LLMs

Causal-Graphs-With-LLMs is a Python project for constructing, evaluating, and visualizing causal graphs using Large Language Models (LLMs). It provides a modular pipeline for graph building, prompt-based extraction, and evaluation against ground truth datasets.

## Project Structure

```
CausalGraphsWithLLMs/
├── __init__.py
├── poetry.lock
├── pyproject.toml
└── causal_graphs_llm/
    ├── __init__.py
    ├── core/
    │   ├── pipeline.py
    │   └── stages/
    │       ├── expansion.py
    │       ├── initialization.py
    │       └── insertion.py
    ├── evaluation/
    │   ├── evaluator.py
    │   ├── visualizer.py
    │   └── ground_truth_graphs/
    │       ├── asia
    │       ├── child
    │       └── neuropathic
    ├── graphs/
    │   └── builder.py
    ├── models/
    │   └── causal.py
    ├── prompts/
    │   ├── __init__.py
    │   ├── extraction_prompt.py
    │   └── initialization_prompt.py
    └── services/
        ├── base_extractor.py
        ├── config.py
        └── extractor.py
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

## License
Specify your license here.

## Contact
Add contact information or links for contributions.

