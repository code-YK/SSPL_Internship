from langchain_groq import ChatGroq
from langchain_core.language_models.chat_models import BaseChatModel

from config import settings
from config import setup_logger

logger = setup_logger(__name__)

def get_llm() -> BaseChatModel:
    """
    Initialize and return a Groq LLM instance.
    """

    logger.info("Initializing Groq LLM")

    llm = ChatGroq(
        api_key=settings.groq_api_key,
        model=settings.groq_model_name,
        temperature=settings.groq_temperature,
        max_tokens=settings.groq_max_tokens,
    )

    logger.info(
        "Groq LLM initialized | model=%s | temperature=%s",
        settings.groq_model_name,
        settings.groq_temperature,
    )

    return llm

llm = get_llm()
