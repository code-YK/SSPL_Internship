def pretty_print(state) -> None:
    """Pretty print the agent state."""
    print("User Inputs:", state.user_inputs)
    print("Route:", state.route)
    print("Result type:", state.result.get("type"))
    print("Content:\n", 
          state.result.get("content") or 
          state.result.get("summary") or 
          state.result.get("notes"))