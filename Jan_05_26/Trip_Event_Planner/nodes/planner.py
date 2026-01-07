from typing import Dict

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.messages import HumanMessage

from llm import llm
from utils import PLANNER_PROMPT
from tools import calculate_trip_days
from states.schemas import ItineraryModel
from config import setup_logger

logger = setup_logger(__name__)


def planner_node(state: Dict) -> Dict:
    """
    Planner agent: creates a day-by-day itinerary.
    """
    logger.info("Running planner agent")

    research = state.get("research_result")
    user_intent = state.get("user_intent")

    if not research or not user_intent:
        raise ValueError("Missing research or user intent in planner node")

    total_days = calculate_trip_days(
        user_intent.start_date,
        user_intent.end_date,
    )

    parser = PydanticOutputParser(pydantic_object=ItineraryModel)

    prompt = f"""
{PLANNER_PROMPT}

User intent:
{user_intent.model_dump()}

Research result:
{research.model_dump()}

Total days: {total_days}

{parser.get_format_instructions()}
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    itinerary = parser.parse(response.content)

    logger.info("Itinerary created successfully")

    return {
        "itinerary": itinerary,
        "current_stage": "planner_review",
    }
