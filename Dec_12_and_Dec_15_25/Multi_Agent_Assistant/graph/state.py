from typing import TypedDict, Annotated, Sequence
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[Sequence, add_messages]

    raw_profile_text: str | None
    extracted_profile: dict | None
    verified_profile: dict | None

    awaiting_confirmation: bool
    confirmation_requested: bool