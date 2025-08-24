from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    def __init__(self):
        self.anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY", None)
        self.gemini_api_key = os.environ.get("GEMINI_API_KEY", None)
        
        self.anthropic_model = "claude-3-7-sonnet-20250219"
        self.gemini_model = "gemini-2.5-pro"  # Fixed: removed the "gemini/" prefix
        
        self.temp = 0.7
        
        # Initialize LLM objects
        self.anthropic_llm = ChatAnthropic(
            temperature=self.temp,
            model_name=self.anthropic_model,
            api_key=self.anthropic_api_key,
            max_tokens=2000,
            max_retries=2
        ) if self.anthropic_api_key else None
        
        self.gemini_llm = ChatGoogleGenerativeAI(
            model=self.gemini_model,
            google_api_key=self.gemini_api_key,
            temperature=self.temp,
            max_output_tokens=2000,
            max_retries=2
        ) if self.gemini_api_key else None
