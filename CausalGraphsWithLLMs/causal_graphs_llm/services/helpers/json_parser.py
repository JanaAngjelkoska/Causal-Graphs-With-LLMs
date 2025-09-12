import json


def validate_json(json_data):
    """
    Validate if the input is a valid JSON object.

    Args:
        json_data (str): The JSON data as a string.

    Returns:
        bool: True if valid JSON, False otherwise.
    """
    try:
        json.loads(json_data)
        return True
    except ValueError:
        return False


def clean_llm_json(raw_content: str):
    """
    Cleans and normalizes LLM output to valid JSON dict.
    - Removes code block markers
    - Converts single quotes to double quotes
    - Strips whitespace
    - Returns a Python dict
    """
    cleaned = raw_content.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("```", 1)[-1]
    cleaned = cleaned.replace("```json", "").replace("```", "").strip()
    cleaned = cleaned.replace("'", '"')
    cleaned = cleaned.replace(",}", "}").replace(",]", "]")
    try:
        return json.loads(cleaned)
    except Exception as e:
        raise ValueError(
            f"Could not clean/parse LLM output as JSON: {e}\nRaw: {raw_content}\nCleaned: {cleaned}"
        )
