from typing import List
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import PydanticOutputParser

from llm import llm
from tools import search_destination_info
from states.schemas import PriceRangeModel
from config import setup_logger
from utils import RESEARCH_COST_PROMPT

logger = setup_logger(__name__)

def extract_price_range(
    query: str,
    category: str
) -> PriceRangeModel:
    """
    Extract price range for a given category using rigid rules.
    """
    logger.info(f"Extracting {category} price range")

    search_result = search_destination_info(query)

    parser = PydanticOutputParser(pydantic_object=PriceRangeModel)

    prompt = f"""
{RESEARCH_COST_PROMPT}

CATEGORY: {category}

WEB DATA:
{search_result}

{parser.get_format_instructions()}
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    price_range = parser.parse(response.content)

    logger.info(
        f"Extracted {category} price range:{price_range.model_dump()}"
    )

    return price_range
