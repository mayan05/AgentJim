from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq
from pydantic import BaseModel
from typing import Literal, List

load_dotenv()

class User(BaseModel):
    name : str | None = None
    age : int | None = None
    gender: List[Literal["Male", "Female", "Non-binary", "Prefer not to say"]] 
    nationality: str | None = None
    height: int | float | None = None

class PlanRequest(BaseModel):
    user: User
    weight: int | float 
    primary_goal: Literal["Weight Loss", "Muscle Gain", "General Fitness", "Strength Training", "Endurance", "Toning"]
    secondary_goal: List[Literal["Weight Loss", "Muscle Gain", "General Fitness", "Strength Training", "Endurance", "Toning", "Flexibility", "Better Sleep", "Stress Relief", "Increased Energy"]] | None
    workout_days: int | None
    session_time: int | None
    additional_details: str | None

class Settings:
    def __init__(self):
        self.gemini_api_key = os.environ.get("GEMINI_API_KEY", None)
        self.groq_api_key = os.environ.get("GROQ_API_KEY", None)
        
        self.gemini_model = "gemini-2.0-flash-exp"
        self.groq_model = "groq/llama-3.3-70b-versatile"

        self.temp = 0.7
        
        # Initialize LLM objects
        self.gemini_llm = ChatGoogleGenerativeAI(
            model=self.gemini_model,
            google_api_key=self.gemini_api_key,
            temperature=self.temp,
            max_output_tokens=2000,
            max_retries=2
        ) if self.gemini_api_key else None

        self.groq_llm = ChatGroq(
            model=self.groq_model,
            api_key=self.groq_api_key,
            temperature=self.temp,
            max_tokens=1000,
            max_retries=2
        ) if self.groq_api_key else None
