from typing import Dict

from langchain_core.messages import HumanMessage

from llm import llm
from states.schemas import FinalTripPlanModel, UserFriendlyTripPlan
from config import setup_logger
from utils import FINAL_PRESENTATION_PROMPT

logger = setup_logger(__name__)


def final_presenter_node(state: Dict) -> Dict:
    """
    Converts the approved structured plan into a user-friendly explanation.
    """
    logger.info("Running final presenter node")

    final_plan: FinalTripPlanModel | None = state.get("final_output")

    if not final_plan:
        raise ValueError("FinalTripPlanModel missing in state")

    prompt = FINAL_PRESENTATION_PROMPT.format(
        structured_plan=final_plan.model_dump()
    )

    response = llm.invoke([HumanMessage(content=prompt)])

    user_friendly_output = UserFriendlyTripPlan(
        title="Your Personalized Trip & Event Plan 🎉",
        summary=response.content,
        itinerary_overview=response.content,
        budget_summary=response.content,
        highlights=response.content,
        important_notes=(
            "All prices are estimates based on current web data. "
            "Actual costs may vary depending on availability and season."
        ),
    )

    logger.info("Final user-friendly output generated")

    return {
        "user_friendly_output": user_friendly_output,
        "final_approved": True,
    }