from datetime import datetime
from typing import List

from config import setup_logger

logger = setup_logger(__name__)


def calculate_trip_days(start_date: str, end_date: str) -> int:
    """
    Calculate total trip duration in days.
    """
    start = datetime.fromisoformat(start_date)
    end = datetime.fromisoformat(end_date)

    total_days = (end - start).days + 1
    logger.info(f"Calculated trip days: {total_days} days")

    return max(total_days, 1)


def validate_event_day(event_day: int, total_days: int) -> bool:
    """
    Ensure event day is within trip duration.
    """
    valid = 1 <= event_day <= total_days
    logger.info(
        f"Validating event day {event_day} / {total_days}: {valid}"
    )
    return valid


def suggest_rest_days(total_days: int, event_day: int) -> List[int]:
    """
    Suggest rest days (typically after the event).
    """
    rest_days = []

    if event_day < total_days:
        rest_days.append(event_day + 1)

    logger.info(f"Suggested rest days: {rest_days}")
    return rest_days
