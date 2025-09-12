BASE_PROMPT = """You're a helpful AI assistant to a causal inference researcher. 
Your task is to analyze the relationships between variables and determine if one variable 
causally affects others based on provided data or logical reasoning. 
Provide a clear and concise response, focusing on the causal impact."""

EXPERT_OPINION_PROMPT = """Causal relationships can be inferred by examining whether changes 
in one variable consistently precede or influence changes in another, while controlling for confounding factors. 
Use this framework to assess the impact."""

def create_extraction_prompt(current_var: str, dependent_vars: list[str]) -> str:
    """
    Creates a prompt to determine if the current variable has a causal effect on other variables.

    Args:
        current_var (str): The variable being analyzed for causal effects.
        dependent_vars (list[str]): List of variables that might be affected.

    Returns:
        str: A formatted prompt for the LLM to evaluate causal relationships, 
             structured for ExpansionResponse parsing.
    """
    vars_list = ", ".join(dependent_vars)
    prompt = (f"{BASE_PROMPT}\n\n{EXPERT_OPINION_PROMPT}\n\nGiven the variable '{current_var}', "
              f"analyze its potential causal effect on the following variables: {vars_list}. "
              f"Determine which of these variables are directly caused by '{current_var}' and return "
              f"your response in a structured JSON format as follows: "
              f"{{\"variable\": \"<the_input_variable>\", \"effects\": [\"<list_of_caused_variables>\"]}}, "
              f"where <list_of_caused_variables> includes only the dependent variables directly caused "
              f"by '{current_var}'. Do not provide any explanation or additional text, send only the JSON object.")
    return prompt