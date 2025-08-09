import os
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class ExtractorConfig(BaseModel):
    """
    Base configuration for agents that interact with the LLM
    """

    model: str = Field(default="gpt-4o-mini", description="Name of the model")
    max_tokens: int = Field(default=512, description="Maximum number of output tokens")
    api_base: str = Field(default="https://api.openai.com/v1", description="Base API endpoint")
    api_key: Optional[str] = Field(default=None, description="OpenAI API key")
    timeout: int = Field(default=30, gt=0, description="Request timeout in seconds")
    max_retries: int = Field(default=3, ge=0, description="Number of times to retry on failure")
    rate_limit_per_minute: Optional[int] = Field(default=None,
                                                 description="Maximum number of requests per minute to the LLM API.")
    temperature: float = Field(default=1.0, ge=0.0, le=2.0, description="Sampling temperature for LLM responses")
    top_p: float = Field(default=1.0, ge=0.0, le=1.0, description="Nucleus sampling parameter")
    presence_penalty: float = Field(default=0.0, ge=-2.0, le=2.0, description="Presence penalty for LLM")
    frequency_penalty: float = Field(default=0.0, ge=-2.0, le=2.0, description="Frequency penalty for LLM")
    stop: Optional[list[str]] = Field(default=None, description="Sequences where the API will stop generating further tokens")

    @field_validator("api_key", mode="before")
    def set_api_key(cls, v):
        api_key = v or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("API key must be provided via parameter or OPENAI_API_KEY environment variable.")
        return api_key