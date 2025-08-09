from collections import deque
from typing import Tuple


def initialization_stage(variables: Tuple[str], edges: Tuple[str]) -> deque:
    """
    Finds variables that are not caused by other variables and adds them to a BFS queue
    variables: list of all variables (strings)
    edges: list of (cause, effect) tuples
    returns: BFS queue initialized with root variables
    :return: queue
    """
    pass
