from typing import List, Dict
from tavily import TavilyClient

from config import settings, setup_logger

logger = setup_logger(__name__)

# Initialize Tavily client once
tavily_client = TavilyClient(api_key=settings.tavily_api_key)


def search_destination_info(query: str) -> Dict:
    """
    Fetch general information about a destination.
    """
    logger.info("Searching destination info: %s", query)

    result = tavily_client.search(
        query=query,
        search_depth=settings.tavily_search_depth,
        max_results=5,
    )

    return result


def search_weather(destination: str, dates: str) -> Dict:
    """
    Fetch weather-related information.
    """
    query = f"Weather in {destination} during {dates}"
    logger.info("Searching weather info: %s", query)

    result = tavily_client.search(
        query=query,
        search_depth=settings.tavily_search_depth,
        max_results=5,
    )

    return result


def search_venues(destination: str, event_type: str) -> List[Dict]:
    """
    Fetch venue and activity options suitable for the event.
    """
    query = f"Best venues for {event_type} in {destination}"
    logger.info("Searching venues: %s", query)

    result = tavily_client.search(
        query=query,
        search_depth=settings.tavily_search_depth,
        max_results=5,
    )

    return result.get("results", [])
