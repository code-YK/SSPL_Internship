import os
from langchain_groq import ChatGroq
from config.settings import settings

def get_groq_llm(modelname: str = "llama-3.1-8b-instant") -> ChatGroq:
    groq_api_key = settings.GROQ_API_KEY
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY is not set in environment variables.")
    llm = ChatGroq(model_name=modelname, api_key=groq_api_key)  
    return llm
