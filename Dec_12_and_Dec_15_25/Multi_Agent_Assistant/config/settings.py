import os
from dotenv import load_dotenv

load_dotenv()

class settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    GROQ_MODEL_NAME: str = os.getenv("GROQ_MODEL_NAME", "mixtral-8x7b-32768")
    MEMORY_FILE: str = os.getenv("MEMORY_FILE", "./data/memory.json")