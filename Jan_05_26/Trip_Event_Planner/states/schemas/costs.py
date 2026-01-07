from pydantic import BaseModel, Field
from typing import Optional

# Model : Price range for a cost (Derived from tavily searches)
class PriceRangeModel(BaseModel):
    category: str = Field(
        description="flight | hotel | event | transport"
    )
    min_price: Optional[int] = Field(
        description="Minimum observed price"
    )
    max_price: Optional[int] = Field(
        description="Maximum observed price"
    )
    currency: Optional[str] = Field(
        description="Currency code (e.g., INR, USD)"
    )
    confidence: str = Field(
        description="low | medium | high"
    )
