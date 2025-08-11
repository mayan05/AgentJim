from pydantic import BaseModel
from langchain_openai import OpenAI
from langchain_anthropic import AnthropicLLM
import os

class Settings(BaseModel):
    openai_api_key: str | None = os.environ.get("OPENAI_API_KEY", None)
    anthropic_api_key: str | None = os.environ.get("ANTHROPIC_API_KEY", None)

    openai_llm: OpenAI = OpenAI(temperature=0.7, model_name="gpt-3.5-turbo-instruct")

    anthropic_llm: AnthropicLLM = AnthropicLLM(temperature=0.7, model_name="claude-2")
