from langchain_core.messages import HumanMessage

from graph import trip_event_graph
from config.logging_config import setup_logger

logger = setup_logger(__name__)


def run():
    logger.info("Starting Trip Event Planner")

    print("\n=== Trip & Event Planner ===\n")

    user_input = input("Describe your trip or event plan:\n> ").strip()

    if not user_input:
        print("No input provided. Exiting.")
        return

    # Initial graph state
    initial_state = {
        "messages": [
            HumanMessage(content=user_input)
        ]
    }

    try:
        result = trip_event_graph.invoke(initial_state)

        print("\n=== Final Plan ===\n")
        final_output = result["user_friendly_output"]

        print("\n" + "=" * 50)
        print(final_output.title)
        print("=" * 50)

        print("\n -->> OVERVIEW <<-- ")
        print(final_output.summary)

        print("\n -->> Itinerary <<-- ")
        print(final_output.itinerary_overview)

        print("\n -->> Budget <<-- ")
        print(final_output.budget_summary)

        print("\n -->> Highlights <<-- ")
        print(final_output.highlights)

        print("\n -->> Important Notes <<-- ")
        print(final_output.important_notes)

    except Exception as e:
        logger.exception("Error while running Trip Event Planner")
        print("\nSomething went wrong. Please check logs.")

    logger.info("Trip Event Planner finished execution")


if __name__ == "__main__":
    run()
