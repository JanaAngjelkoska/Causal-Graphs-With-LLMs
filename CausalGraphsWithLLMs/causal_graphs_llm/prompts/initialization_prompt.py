BASE_PROMPT = """
You're a helpful AI assistant to a causal inference researcher. 
Your task is to analyze the relationships between variables and identify which variables serve as root nodes
 (those not caused by any other variables) based on provided data or logical reasoning.
"""

EXPERT_OPINION_PROMPT = """
Independent variables in a causal graph are those that have no incoming causal edges,
meaning no other variables directly cause them. 
Dependent variables are those that are directly caused by one or more other variables.
"""



def create_initialization_prompt(query: str) -> str:
    """
    Creates a prompt to determine which variables are independent (root variables with no causes)
    or dependent.

    Args:
        variables (list[str]): List of all variables to classify.

    Returns:
        str: A formatted prompt for the LLM to evaluate variable independence.
    """
    prompt = (f"{BASE_PROMPT}\n\n{EXPERT_OPINION_PROMPT}\n\nGiven the following query: "
              f"{query}, classify each variable as 'INDEPENDENT' if it has no causes "
              f"(i.e., no other variables directly affect it) or another label (e.g., 'DEPENDENT') "
              f"if it is caused by others. Provide your answer in a structured format as a JSON object "
              f"with the following format: {{'root_variables': {{'A': 'INDEPENDENT', 'B': 'DEPENDENT'}}}}. "
              f"Respond only with a valid JSON object as specified, using double quotes for all keys and string values, and nothing else.")
    return prompt
