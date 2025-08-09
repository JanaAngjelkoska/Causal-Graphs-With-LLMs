from pydantic import BaseModel
from typing import List, Tuple


class InitializationResponse(BaseModel):
    root_variables = List[str]


class ExpansionResponse(BaseModel):
    variable: str
    effects: List[str]


class InsertionResponse(BaseModel):
    edges: List[Tuple[str, str]]
