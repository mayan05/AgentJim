from pydantic import BaseModel
from langchain_openai import OpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
import os

class Settings(BaseModel):
    openai_api_key: str | None = os.environ.get("OPENAI_API_KEY", None)
    anthropic_api_key: str | None = os.environ.get("ANTHROPIC_API_KEY", None)
    gemini_api_key: str | None = os.environ.get("GEMINI_API_KEY", None)

    openai_model: str = "gpt-3.5-turbo-instruct"
    anthropic_model: str = "claude-2"
    gemini_model: str = "gemini-2.5-pro"

    temp: float = 0.7

    openai_llm: OpenAI = OpenAI(temperature=temp, 
    model_name=openai_model, max_tokens=2000, 
    api_key=openai_api_key)

    anthropic_llm: ChatAnthropic = ChatAnthropic(temperature=temp, model_name=anthropic_model, 
    api_key=anthropic_api_key, 
    max_tokens=2000)

    gemini_llm: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
        model=gemini_model,
        google_api_key=gemini_api_key,
        temperature=temp,
        max_output_tokens=2000,
        max_retries=2
    )
