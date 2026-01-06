from pydantic import BaseModel, Field
from typing import Optional, List

# Model for user intent in trip planning
# messy user input -> structured intent
class UserIntentModel(BaseModel):
    destination: Optional[str] = Field(
        default=None, description="Preferred destination (optional)"
    )
    start_date: Optional[str] = Field(
        default=None, description="Trip start date (YYYY-MM-DD)"
    )
    end_date: Optional[str] = Field(
        default=None, description="Trip end date (YYYY-MM-DD)"
    )
    budget: Optional[int] = Field(
        default=None, description="Total budget in local currency"
    )
    event_type: str = Field(
        ..., description="Type of event (birthday, anniversary, wedding, etc.)"
    )
    group_size: int = Field(
        ..., description="Number of travelers"
    )
    preferences: List[str] = Field(
        default_factory=list, description="User preferences (food, pace, etc.)"
    )
