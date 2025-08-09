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
