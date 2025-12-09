from .state import Agentstate

WRITING_KEYWORDS = ["write", "draft", "compose", "email", "message"]
RESEARCH_KEYWORDS = ["research", "latest", "who", "what", "when", "study", "papers"]
PLANNER_KEYWORDS = ["plan", "schedule", "todo", "tasks", "breakdown"]

def router(state: Agentstate) -> str:
    """Route the user input to the appropriate agent based on keywords."""
    input_lower = state.user_inputs.lower()
    
    if any(keyword in input_lower for keyword in WRITING_KEYWORDS):
        return "writer"
    elif any(keyword in input_lower for keyword in RESEARCH_KEYWORDS):
        return "research"   # FIXED
    elif any(keyword in input_lower for keyword in PLANNER_KEYWORDS):
        return "planner"
    else:
        return "general"
