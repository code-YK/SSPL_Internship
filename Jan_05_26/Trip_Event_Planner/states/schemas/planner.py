from pydantic import BaseModel, Field
from typing import List, Optional

# Model : Day plan within the itinerary
class DayPlanModel(BaseModel):
    day_number: int
    date: Optional[str]
    activities: List[str]
    is_event_day: bool = False
    notes: Optional[str] = None

# Model : Final Itinerary output
class ItineraryModel(BaseModel):
    total_days: int
    days: List[DayPlanModel]
    event_day: int
    event_details: str
    rest_days: List[int] = Field(default_factory=list)
    assumptions: List[str] = Field(default_factory=list)
