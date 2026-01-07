from typing import Dict

from states.schemas import ReviewDecisionModel
from config import setup_logger

logger = setup_logger(__name__)


def review_node(stage: str):
    """
    Human-in-the-loop review node factory.

    stage: "research" | "planner" | "pricing"
    """

    def _review(state: Dict) -> Dict:
        logger.info(f"Entering review node for stage: {stage}")

        print("\n" + "=" * 50)
        print(f"REVIEW STAGE: {stage.upper()}")
        print("=" * 50)

        # Show relevant output summary
        if stage == "research":
            print("\nResearch Summary:")
            print(state.get("research_result"))

        elif stage == "planner":
            print("\nItinerary:")
            print(state.get("itinerary"))

        elif stage == "pricing":
            print("\nPricing Details:")
            print(state.get("pricing"))

        print("\n--- Approval ---")
        decision = input("Do you approve this stage? (yes/no): ").strip().lower()

        approved = decision == "yes"
        feedback = None
        revision_target = None

        if not approved:
            feedback = input("Please describe what you want to change: ").strip()
            revision_target = stage

        review = ReviewDecisionModel(
            approved=approved,
            feedback=feedback,
            revision_target=revision_target,
        )

        logger.info(
            f"Review decision | stage={stage} | approved={approved}"
        )

        return {
            f"{stage}_review": review
        }

    return _review
