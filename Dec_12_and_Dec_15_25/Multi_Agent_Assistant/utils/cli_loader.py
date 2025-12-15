from langchain_core.messages import HumanMessage
from utils.file_loader import load_text_file
from graph import build_graph
from agents import assistant_agent

def run_profile_ingestion():
    """
    MODE 1: Profile ingestion + HITL confirmation
    """
    print("\n--- PROFILE INGESTION MODE ---\n")

    app = build_graph()

    profile_text = load_text_file("sample_profile.txt")

    state = {
        "messages": [],
        "raw_profile_text": profile_text,
        "extracted_profile": None,
        "verified_profile": None,
        "awaiting_confirmation": False,
        "confirmation_requested": False
    }

    # Step 1: Run extractor + validator (will stop if HITL needed)
    state = app.invoke(state)

    print("Agent:", state["messages"][-1].content)

    # Step 2: HITL loop
    while state["awaiting_confirmation"]:
        user_input = input("You (confirm): ")

        state = app.invoke({
            **state,
            "messages": state["messages"] + [HumanMessage(content=user_input)]
        })

        print("Agent:", state["messages"][-1].content)

    print("\nProfile successfully stored in memory.\n")


def run_chat_mode():
    """
    MODE 2: Normal assistant chat (uses stored memory)
    """
    print("\n--- CHAT MODE (type 'exit' to quit) ---\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = assistant_agent({
            "messages": [HumanMessage(content=user_input)]
        })

        print("Agent:", response["messages"][-1].content)