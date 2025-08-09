from collections import deque

from click import Tuple


def expansion_stage(queue: deque, edges: Tuple[str], visited: Tuple[str]):
    """
    Finds which variables are caused by the first variable in the queue,
    queue: deque of variables to process
    edges: list of (cause, effect) tuples
    visited: set of already processed variables
    :return: cause, list_of_effects
    """
    pass

# so here's the flow:
#
# Firstly, the service should be configured to communicate with an LLM (configured agent we call "extractor") and in the pipeline.py we run the stages:
#
# 1. User baseline query (a text with variables and causes)
# 2. Creating a better prompt in initialization_prompt.py with create_initialization_prompt()
# 3. Send the initialization prompt to a LLM service
# 4. using pydantic, structure the output in a JSON of the LLM service -> these are independent vars,  format with pydantic from causal.py
# 5. Initialization stage ->  variables that are not caused by other variables and adds them to a BFS queue
# 6. Creating a better prompt in expansion_prompt.py with create_expansion_prompt()
# 7. Send the expansion prompt to a LLM service
# 8. Extract the information in a JSON format with pydantic from causal.py
# 9. Use the expansion.py to use the JSON format -> Finds which variables are caused by the first variable in the queue