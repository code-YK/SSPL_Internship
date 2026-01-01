from utils import run_profile_ingestion, run_chat_mode
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    run_profile_ingestion()
    run_chat_mode()
