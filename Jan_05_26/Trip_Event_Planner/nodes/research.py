from typing import Dict

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.messages import HumanMessage

from llm import llm
from utils import RESEARCH_PROMPT
from tools import search_destination_info, search_weather, search_venues, extract_price_range
from states.schemas import ResearchOutputModel
from config import setup_logger

logger = setup_logger(__name__)


def research_node(state: Dict) -> Dict:
    """
    Research agent: collects real-world info using tools and structures it.
    """
    logger.info("Running research agent")

    user_intent = state.get("user_intent")
    if not user_intent:
        raise ValueError("User intent missing in research node")

    destination = user_intent.destination or "best suitable destination"
    event_type = user_intent.event_type
    dates = f"{user_intent.start_date} to {user_intent.end_date}"

    # Tool calls
    destination_info = search_destination_info(destination)
    weather_info = search_weather(destination, dates)
    venue_info = search_venues(destination, event_type)

    # Cost extraction
    flight_prices = extract_price_range(
        query=f"average flight cost to {destination}",
        category="flight",
    )

    hotel_prices = extract_price_range(
        query=f"average hotel cost per night in {destination}",
        category="hotel",
    )

    event_prices = extract_price_range(
        query=f"{event_type} venue cost in {destination}",
        category="event",
    )

    transport_prices = extract_price_range(
        query=f"local transport cost per day in {destination}",
        category="transport",
    )

    # LLM reasoning (NO COSTS)
    parser = PydanticOutputParser(pydantic_object=ResearchOutputModel)

    prompt = f"""
{RESEARCH_PROMPT}

User intent:
{user_intent.model_dump()}

Destination info:
{destination_info}

Weather info:
{weather_info}

Venue info:
{venue_info}

IMPORTANT:
- Do NOT invent prices.
- Price fields will be injected separately.

{parser.get_format_instructions()}
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    llm_output = parser.parse(response.content)

    # Merge cost data
    research_result = ResearchOutputModel(
        **llm_output.model_dump(exclude={
            "flight_price_range",
            "hotel_price_range",
            "event_price_range",
            "transport_price_range",
        }),
        flight_price_range=flight_prices,
        hotel_price_range=hotel_prices,
        event_price_range=event_prices,
        transport_price_range=transport_prices,
    )

    logger.info("Research completed successfully")

    return {
        "research_result": research_result,
        "current_stage": "research_review",
    }