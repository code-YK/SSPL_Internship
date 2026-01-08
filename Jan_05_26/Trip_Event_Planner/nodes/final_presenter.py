from typing import Dict

from langchain_core.messages import HumanMessage

from llm import llm
from states.schemas import FinalTripPlanModel, UserFriendlyTripPlan
from config import setup_logger
from utils import FINAL_PRESENTATION_PROMPT

logger = setup_logger(__name__)


def final_presenter_node(state: Dict) -> Dict:
    """
    Assembles the final structured plan if needed and converts it
    into a user-friendly explanation.
    """
    logger.info("Running final presenter node")

    # Assemble FinalTripPlanModel if missing
    final_plan: FinalTripPlanModel | None = state.get("final_output")

    if final_plan is None:
        logger.info("FinalTripPlanModel missing. Assembling inside final presenter.")

        try:
            final_plan = FinalTripPlanModel(
                user_intent=state["user_intent"],
                research_summary=state["research_result"],
                itinerary=state["itinerary"],
                pricing=state["pricing"],
            )
            state["final_output"] = final_plan
        except KeyError as e:
            raise ValueError(
                f"Cannot assemble FinalTripPlanModel. Missing state field: {e}"
            )

    prompt = FINAL_PRESENTATION_PROMPT.format(
        structured_plan=final_plan.model_dump()
    )

    response = llm.invoke([HumanMessage(content=prompt)])

    user_friendly_output = UserFriendlyTripPlan(
        title="Your Personalized Trip & Event Plan",
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

    state["user_friendly_output"] = user_friendly_output
    state["final_approved"] = True

    return state
