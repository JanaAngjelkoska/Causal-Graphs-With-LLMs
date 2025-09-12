import logging
from collections import deque
from typing import List

logger = logging.getLogger(__name__)


def expansion_stage(variable: str, effects: List[str], visited: deque[str]):
    """
    Finds which variables are caused by the first variable in the queue.
    Returns:
         cause, list_of_effects
    """
    logger.info(f"Expanding variable: {variable}")
    logger.info(f"Current effects: {effects}")
    logger.info(f"Visited before: {list(visited)}")

    visited.remove(variable)
    for effect in effects:
        visited.append(effect)

    logger.info(f"Visited after: {list(visited)}")
    return visited
