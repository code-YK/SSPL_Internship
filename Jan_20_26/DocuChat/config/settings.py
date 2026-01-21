import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", 0.7))

debug = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
