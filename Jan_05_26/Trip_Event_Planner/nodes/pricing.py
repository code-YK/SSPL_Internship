from typing import Dict

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.messages import HumanMessage

from llm import llm
from tools.pricing import estimate_from_range
from tools.research_cost import extract_price_range
from utils import PRICING_PROMPT
from tools import calculate_total_cost, apply_budget_buffer, identify_cost_risks, estimate_from_range
from states.schemas import PricingModel
from config import setup_logger

logger = setup_logger(__name__)

def pricing_node(state: Dict) -> Dict:
    """
    Pricing agent: converts research price ranges into final estimates.
    """
    logger.info("Running pricing agent")

    research = state.get("research_result")
    itinerary = state.get("itinerary")
    user_intent = state.get("user_intent")

    if not research or not itinerary or not user_intent:
        raise ValueError("Missing required data for pricing")

    total_days = itinerary.total_days

    # Estimate costs from ranges
    flight_cost = estimate_from_range(
        research.flight_price_range.min_price,
        research.flight_price_range.max_price,
    )

    hotel_per_night = estimate_from_range(
        research.hotel_price_range.min_price,
        research.hotel_price_range.max_price,
    )
    hotel_cost = hotel_per_night * total_days

    event_cost = estimate_from_range(
        research.event_price_range.min_price,
        research.event_price_range.max_price,
    )

    transport_per_day = estimate_from_range(
        research.transport_price_range.min_price,
        research.transport_price_range.max_price,
    )
    transport_cost = transport_per_day * total_days

    # Cost breakdown
    base_costs = {
        "flights": flight_cost,
        "accommodation": hotel_cost,
        "local_transport": transport_cost,
        "event_cost": event_cost,
    }

    total_cost = calculate_total_cost(base_costs)
    buffer_amount = apply_budget_buffer(total_cost)
    final_cost = total_cost + buffer_amount

    risks = identify_cost_risks(
        total_cost=final_cost,
        budget=user_intent.budget or final_cost,
    )

    # LLM explanation (not math)
    parser = PydanticOutputParser(pydantic_object=PricingModel)

    prompt = f"""
{PRICING_PROMPT}

Cost breakdown:
{base_costs}

Buffer added: {buffer_amount}
Final estimated cost: {final_cost}

Risks:
{risks}

IMPORTANT:
- Do not change numbers
- Only explain and structure

{parser.get_format_instructions()}
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    pricing = parser.parse(response.content)

    logger.info("Pricing completed successfully")

    return {
        "pricing": pricing,
        "current_stage": "pricing_review",
    }