import json
from langchain_core.messages import AIMessage

MEMORY_FILE = "memory/profile_memory.json"

def memory_keeper_agent(state):
    profile = state.get("verified_profile")

    # SAFETY CHECK
    if not profile:
        return {
            "messages": [AIMessage(content="No verified profile to store.")]
        }

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4, ensure_ascii=False)

    return {
        "messages": [AIMessage(content="Profile saved to long-term memory.")]
    }
