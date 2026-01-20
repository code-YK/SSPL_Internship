from langchain_groq import ChatGroq
from langchain_core.language_models.chat_models import BaseChatModel

from config.settings import API_KEY, MODEL_NAME, DEFAULT_TEMPERATURE
from config.logger_config import setup_logger

logger = setup_logger(__name__)

def get_llm() -> BaseChatModel:
    '''Initialize and return the Groq Chat LLM instance.'''

    logger.info(f"Initializing Groq Chat LLM with model: {MODEL_NAME}")

    llm = ChatGroq(
        model_name=MODEL_NAME,
        api_key=API_KEY,
        temperature=DEFAULT_TEMPERATURE,
        max_retries=3,
        timeout=60,
    )

    logger.info("Groq Chat LLM initialized successfully.")
    return llm

llm = get_llm()