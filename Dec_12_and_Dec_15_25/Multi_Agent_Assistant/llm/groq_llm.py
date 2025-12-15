from langchain_groq import ChatGroq
from config.settings import settings

def get_groq_llm():
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=settings.GROQ_MODEL_NAME,
        temperature=0
    )
