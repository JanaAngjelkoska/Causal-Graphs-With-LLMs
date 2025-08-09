from typing import List, Tuple
from pydantic import BaseModel, Field

class InitializationResponse(BaseModel):
    root_variables: List[str] = Field(..., description="Variables that have no causes")

class ExpansionResponse(BaseModel):
    variable: str = Field(..., description="Variable being expanded")
    effects: List[str] = Field(..., description="Variables directly caused by 'variable'")

class InsertionResponse(BaseModel):
    edges: List[Tuple[str, str]] = Field(..., description="List of (cause, effect) edges")
