from pydantic import BaseModel
from langchain_openai import OpenAI
from langchain_anthropic import AnthropicLLM
import os

class Settings(BaseModel):
    openai_api_key: str | None = os.environ.get("OPENAI_API_KEY", None)
    anthropic_api_key: str | None = os.environ.get("ANTHROPIC_API_KEY", None)

    openai_model: str = "gpt-3.5-turbo-instruct"
    anthropic_model: str = "claude-2"

    temp: float = 0.7

    openai_llm: OpenAI = OpenAI(temperature=temp, model_name=openai_model, max_tokens=2000, api_key=openai_api_key)

    anthropic_llm: AnthropicLLM = AnthropicLLM(temperature=temp, model_name=anthropic_model, api_key=anthropic_api_key, max_tokens=2000)
