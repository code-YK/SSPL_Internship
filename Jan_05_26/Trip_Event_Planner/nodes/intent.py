from typing import Dict

from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import PydanticOutputParser

from llm import llm
from utils import INTENT_PROMPT
from states.schemas import UserIntentModel
from config import setup_logger

logger = setup_logger(__name__)

# Extract structured user intent from the latest user message.

def intent_node(state: Dict) -> Dict:

    logger.info("Running intent extraction node")

    messages = state.get("messages", [])
    if not messages:
        raise ValueError("No messages found for intent extraction")

    latest_user_message = messages[-1].content

    parser = PydanticOutputParser(pydantic_object=UserIntentModel)

    prompt = (
        INTENT_PROMPT
        + "\n\nUser message:\n"
        + latest_user_message
        + "\n\n"
        + parser.get_format_instructions()
    )

    response = llm.invoke([HumanMessage(content=prompt)])

    intent = parser.parse(response.content)

    logger.info("Extracted user intent successfully")

    return {
        "user_intent": intent,
        "current_stage": "research",
    }
