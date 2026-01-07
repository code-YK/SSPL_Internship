from typing import List
from langchain_core.messages import BaseMessage
from config import settings, setup_logger

logger = setup_logger(__name__)

def rolling_message_reducer(
    existing: List[BaseMessage],
    incoming: List[BaseMessage]
) -> List[BaseMessage]:
    
    """
    Reducer to keep only the last N messages
    defined by MAX_MESSAGE_WINDOW.
    Currently MAX_MESSAGE_WINDOW is set to 12.
    """
    combined = existing + incoming
    max_window = settings.max_message_window

    if len(combined) > max_window:
        logger.debug(
            f"Reducing messages from {len(combined)} to last {max_window}"
        )
        return combined[-max_window:]

    return combined
