import json
import re
from langchain_core.messages import AIMessage
from llm.groq_llm import get_groq_llm
from config import EXTRACTION_PROMPT

llm = get_groq_llm()


def extract_json(text: str) -> dict:
    """
    Safely extract JSON from LLM output.

    Handles:
    - JSON inside markdown code fences
    - Raw JSON inside text

    Never uses eval() for security reasons.
    """

    # Case 1: JSON inside ```json ... ```
    code_fence_match = re.search(
        r"```(?:json)?\s*(\{.*?\})\s*```",
        text,
        re.DOTALL
    )
    if code_fence_match:
        return json.loads(code_fence_match.group(1))

    # Case 2: Raw JSON in text
    raw_json_match = re.search(
        r"(\{.*\})",
        text,
        re.DOTALL
    )
    if raw_json_match:
        return json.loads(raw_json_match.group(1))

    raise ValueError("No valid JSON object found in LLM output")


def extractor_agent(state):
    """
    Agent 1: Extractor Agent

    Responsibilities:
    - Read raw profile text from state
    - Use LLM to extract structured information
    - Store extracted data as UNVERIFIED memory
    """

    # If extraction already happened, skip
    if state.get("extracted_profile") is not None:
        return {}
    
    # Read raw profile text from LangGraph state
    profile_text = state["raw_profile_text"]

    # Send extraction prompt to LLM
    response = llm.invoke(
        EXTRACTION_PROMPT.format(profile_text=profile_text)
    )

    # Safely parse JSON from LLM output
    extracted_data = extract_json(response.content)

    # Return updated state
    return {
        # Inform downstream agents that extraction is done
        "messages": [AIMessage(content="Profile information extracted.")],

        # Store extracted data (still unverified)
        "extracted_profile": extracted_data,

        # Signal that human confirmation is required
        "awaiting_confirmation": True,

        # Confirmation request is handled in validator agent
        "confirmation_requested": False
    }