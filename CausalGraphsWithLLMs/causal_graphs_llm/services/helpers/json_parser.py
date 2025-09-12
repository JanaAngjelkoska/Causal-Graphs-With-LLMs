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
    - Removes code block markers (``` and ```json)
    - Strips whitespace
    - Tries to parse as JSON
    - If parsing fails, tries to replace single quotes with double quotes and parse again
    - Returns a Python dict
    """
    cleaned = raw_content.strip()
    # Remove code block markers and language tags
    if cleaned.startswith('```json'):
        cleaned = cleaned[len('```json'):].strip()
    elif cleaned.startswith('```'):
        cleaned = cleaned[len('```'):].strip()
    if cleaned.endswith('```'):
        cleaned = cleaned[:-3].strip()
    # Try parsing as JSON
    try:
        return json.loads(cleaned)
    except Exception:
        # Try replacing single quotes with double quotes and parse again
        cleaned2 = cleaned.replace("'", '"')
        try:
            return json.loads(cleaned2)
        except Exception as e:
            raise ValueError(f"Could not clean/parse LLM output as JSON: {e}\nRaw: {raw_content}\nCleaned: {cleaned2}")


def clean_llm_content(content: str) -> str:
    """
    Cleans LLM response content by removing markdown code block formatting and language tags.
    Returns a cleaned string suitable for JSON parsing.
    """
    if content is None:
        return ''
    cleaned = content.strip()
    if cleaned.startswith('```json'):
        cleaned = cleaned[len('```json'):].strip()
    elif cleaned.startswith('```'):
        cleaned = cleaned[len('```'):].strip()
    if cleaned.endswith('```'):
        cleaned = cleaned[:-3].strip()
    return cleaned
