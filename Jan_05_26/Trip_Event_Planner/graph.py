from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage

from states.main_state import TripEventState
from states.schemas import FinalTripPlanModel

from nodes.intent import intent_node
from nodes.research import research_node
from nodes.planner import planner_node
from nodes.pricing import pricing_node
from nodes.review import review_node
from nodes.final_presenter import final_presenter_node

from config import setup_logger

logger = setup_logger(__name__)


# Graph Initialization
graph = StateGraph(TripEventState)


# Register Nodes
# Core agent nodes
graph.add_node("intent", intent_node)
graph.add_node("research", research_node)
graph.add_node("planner", planner_node)
graph.add_node("pricing", pricing_node)

# Human-in-the-loop review nodes
graph.add_node("research_review", review_node("research"))
graph.add_node("planner_review", review_node("planner"))
graph.add_node("pricing_review", review_node("pricing"))

# Final presentation node
graph.add_node("final_presenter", final_presenter_node)


# Conditional Logic
def route_after_research_review(state: TripEventState) -> str:
    """
    After research review, if approved move to planner, else loop back to research.
    """
    review = state.get("research_review")

    try:
        if review and review.approved:
            logger.info("Research approved. Moving to planner.")
            return "planner"
    except Exception as e:
        logger.error(f"Error during research review routing: {e}")

    logger.info("Research rejected. Looping back to research.")
    return "research"


def route_after_planner_review(state: TripEventState) -> str:
    """
    After planner review, if approved move to pricing, else loop back to planner.
    """
    review = state.get("planner_review")

    try:         
        if review and review.approved:
            logger.info("Planner approved. Moving to pricing.")
            return "pricing"
    except Exception as e:
        logger.error(f"Error during planner review routing: {e}")

    logger.info("Planner rejected. Looping back to planner.")
    return "planner"


def route_after_pricing_review(state: TripEventState) -> str:
    """
    After pricing review, If approved, assemble final output and move to presenter. 
    Else, loop back to pricing.
    """
    review = state.get("pricing_review")

    try:  
        if review and review.approved:
            logger.info("Pricing approved. Assembling final trip plan.")

            state["final_output"] = FinalTripPlanModel(
                user_intent=state["user_intent"],
                research_summary=state["research_result"],
                itinerary=state["itinerary"],
                pricing=state["pricing"],
            )

            return "final_presenter"
    except Exception as e:
        logger.error(f"Error during pricing review routing: {e}")
    
    logger.info("Pricing rejected. Looping back to pricing.")
    return "pricing"


# Graph Edges
# Entry point
graph.set_entry_point("intent")

# Linear flow
graph.add_edge("intent", "research")
graph.add_edge("research", "research_review")

# Research review -> conditional
graph.add_conditional_edges(
    "research_review",
    route_after_research_review,
    {
        "planner": "planner",
        "research": "research",
    }
)

# Planner flow
graph.add_edge("planner", "planner_review")

graph.add_conditional_edges(
    "planner_review",
    route_after_planner_review,
    {
        "pricing": "pricing",
        "planner": "planner",
    }
)

# Pricing flow
graph.add_edge("pricing", "pricing_review")

graph.add_conditional_edges(
    "pricing_review",
    route_after_pricing_review,
    {
        "final_presenter": "final_presenter",
        "pricing": "pricing",
    }
)

# Final presenter -> END
graph.add_edge("final_presenter", END)


# Compile Graph
trip_event_graph = graph.compile()
