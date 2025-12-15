from langchain_core.messages import AIMessage, HumanMessage
from config import VALIDATION_QUESTION

def validator_agent(state):
    extracted = state["extracted_profile"]
    messages = state["messages"]

    awaiting = state.get("awaiting_confirmation", False)
    asked = state.get("confirmation_requested", False)

    last_msg = messages[-1]

    # STEP 1: Ask confirmation ONLY ONCE
    if awaiting and not asked:
        return {
            "messages": [AIMessage(
                content=VALIDATION_QUESTION.format(extracted_content=extracted)
            )],
            "confirmation_requested": True
        }

    # STEP 2: Process human response
    if awaiting and asked and isinstance(last_msg, HumanMessage):
        user_input = last_msg.content.strip().lower()

        # Case: user confirms
        if user_input == "yes":
            return {
                "verified_profile": extracted,
                "awaiting_confirmation": False,
                "messages": [AIMessage(
                    content="Profile verified successfully."
                )]
            }

        # Case: user corrects
        else:
            corrected = eval(last_msg.content)  # HITL, controlled input
            return {
                "verified_profile": corrected,
                "awaiting_confirmation": False,
                "messages": [AIMessage(
                    content="Profile corrected and verified successfully."
                )]
            }

    # STEP 3: Waiting state (do nothing)
    return {}
