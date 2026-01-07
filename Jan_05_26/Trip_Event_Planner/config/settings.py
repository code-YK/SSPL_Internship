from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    # App Environment
    debug: bool = True

    # Groq LLM
    groq_api_key: str
    groq_model_name: str = "llama-3.3-70b-versatile"
    groq_temperature: float = 0.3
    groq_max_tokens: int = 2048

    # Tavily Search
    tavily_api_key: str
    tavily_search_depth: str = "basic"

    # LangSmith Tracing
    langchain_tracing_v2: bool = True
    langchain_api_key: str
    langchain_project: str = "trip-event-planner"
    langchain_endpoint: str = "https://api.smith.langchain.com"

    # Memory / Reducers
    max_message_window: int = 12
    
    # Planner / Pricing Defaults
    default_budget_buffer_percent: int = 10
    max_planner_retries: int = 3
    max_research_retries: int = 3

    # Pydantic Settings Config
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
