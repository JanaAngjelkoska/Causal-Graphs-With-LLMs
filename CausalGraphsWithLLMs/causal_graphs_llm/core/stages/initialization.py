import logging

logger = logging.getLogger(__name__)

def initialization_stage(variables: dict):
    """
    Finds variables that are not caused by other variables and adds them to a BFS queue.

    variables: list of all variables (strings)
    edges: list of (cause, effect) tuples
    returns: BFS queue initialized with root variables
    Returns:
        queue
    """
    independent_variables = []
    dependent_variables = []
    for variable, description in variables.items():
        if description == "INDEPENDENT":
            independent_variables.append(variable)
            logger.info(f"Variable '{variable}' classified as INDEPENDENT.")
        else:
            dependent_variables.append(variable)
            logger.info(f"Variable '{variable}' classified as DEPENDENT.")

    logger.info(f"Independent variables: {independent_variables}")
    logger.info(f"Dependent variables: {dependent_variables}")
    return independent_variables, dependent_variables




