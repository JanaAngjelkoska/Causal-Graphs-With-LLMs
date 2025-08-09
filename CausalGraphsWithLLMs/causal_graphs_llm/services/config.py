import os
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class ExtractorConfig(BaseModel):
    """
    Configuration for any LLM extractor
    """

    model: str = Field(default="gpt-4o-mini", description="Name of the model")
    max_tokens: int = Field(default=512, description="Maximum number of output tokens")
    api_base: str = Field(default="https://api.openai.com/v1", description="Base API endpoint")
    api_key: Optional[str] = Field(default=None, description="OpenAI API key")
    timeout: int = Field(default=30, gt=0, description="Request timeout in seconds")
    max_retries: int = Field(default=3, ge=0, description="Number of times to retry on failure")
    rate_limit_per_minute: Optional[int] = Field(default=None,
                                                 description="Maximum number of requests per minute to the LLM API.")

    @field_validator("api_key", mode="before")
    def set_api_key(cls, v):
        """
        Ensure api_key is set, falling back to environment variable.
        """
        return v or os.getenv("OPENAI_API_KEY")
