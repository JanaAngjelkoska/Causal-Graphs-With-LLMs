from typing import Optional
from pydantic import BaseModel, Field


class ExtractorConfig(BaseModel):
    """
    Configuration for interacting with an LLM for causal graph extraction.
    """

    endpoint: str = Field(
        default="https://models.github.ai/inference",
        description="API endpoint for the LLM service."
    )

    model: str = Field(
            default="meta/Llama-4-Scout-17B-16E-Instruct",
        description="LLM model name to use for queries."
    )

    max_tokens: int = Field(
        default=2048,
        description="Maximum number of tokens to generate per query."
    )

    temperature: float = Field(
        default=0.8,
        ge=0.0,
        le=2.0,
        description="Sampling temperature. 0.0 for deterministic output."
    )

    top_p: float = Field(
        default=0.1,
        ge=0.0,
        le=1.0,
        description="Top-p sampling for output diversity."
    )

    stop: Optional[list[str]] = Field(
        default=None,
        description="Optional stop sequences for generation."
    )
