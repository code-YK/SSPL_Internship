from pydantic import BaseModel, Field
from typing import List

# Model : Cost breakdown within pricing
class CostBreakdownModel(BaseModel):
    flights: int
    accommodation: int
    local_transport: int
    event_cost: int
    buffer: int

# Model : Pricing output
class PricingModel(BaseModel):
    cost_breakdown: CostBreakdownModel
    total_estimated_cost: int
    risk_factors: List[str] = Field(default_factory=list)
    cost_saving_options: List[str] = Field(default_factory=list)
    confidence_level: str = Field(
        description="low / medium / high"
    )
