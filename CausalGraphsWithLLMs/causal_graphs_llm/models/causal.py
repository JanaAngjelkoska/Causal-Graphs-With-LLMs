from typing import List
from pydantic import BaseModel, Field

class InitializationResponse(BaseModel):
    """
    Returns root variables marked as dependent or independent
    """
    root_variables: dict[str, str] = (
        Field(description="Dictionary of variables with their classifications."))

class ExpansionResponse(BaseModel):
    """
    Returns a variable and its direct effects.
    """
    variable: str = Field(description="Variable being expanded")
    effects: List[str] = Field(description="Variables caused by 'variable'")

class InsertionResponse(BaseModel):
    """
    Returns newly inserted edges into the causal graph.
    """
    edges: dict[str, str] = Field(description="List of (cause, effect) edges")
