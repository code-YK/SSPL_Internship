from pydantic import BaseModel, Field
from typing import List, Optional
from states.schemas.costs import PriceRangeModel

# Model : Research for venue
class VenueOptionModel(BaseModel):
    name: str
    venue_type: str = Field(
        description="hotel, resort, restaurant, activity venue"
    )
    estimated_price_per_day: int
    suitable_for_event: bool

# Model : Research phase output
class ResearchOutputModel(BaseModel):
    confirmed_destination: str
    weather_summary: str
    best_travel_window: str

    venue_options: List[VenueOptionModel]

    # NEW: Cost estimates for different categories
    flight_price_range: Optional[PriceRangeModel]
    hotel_price_range: Optional[PriceRangeModel]
    event_price_range: Optional[PriceRangeModel]
    transport_price_range: Optional[PriceRangeModel]

    constraints: List[str] = Field(default_factory=list)
    assumptions: List[str] = Field(default_factory=list)