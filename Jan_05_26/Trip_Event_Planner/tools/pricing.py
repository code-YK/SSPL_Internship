from typing import Dict, List

from config import settings, setup_logger

logger = setup_logger(__name__)


def calculate_total_cost(cost_breakdown: Dict[str, int]) -> int:
    """
    Calculate total cost from breakdown.
    """
    total = sum(cost_breakdown.values())
    logger.info(f"Calculated total cost: {total}")
    return total


def apply_budget_buffer(total_cost: int) -> int:
    """
    Apply buffer percentage to total cost.
    """
    buffer_amount = (total_cost * settings.default_budget_buffer_percent) // 100
    logger.info(f"Applied buffer: {buffer_amount}")
    return buffer_amount


def identify_cost_risks(total_cost: int, budget: int) -> List[str]:
    """
    Identify potential cost risks.
    """
    risks = []

    if total_cost > budget:
        risks.append("Total cost exceeds budget")

    if total_cost > budget * 0.9:
        risks.append("Budget margin is very tight")

    logger.info(f"Identified cost risks: {risks}")
    return risks


def estimate_from_range(min_price: int, max_price: int) -> int:
    """
    midpoint estimate.
    """
    return (min_price + max_price) // 2
