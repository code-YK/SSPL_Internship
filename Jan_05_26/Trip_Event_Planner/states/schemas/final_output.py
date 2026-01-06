from pydantic import BaseModel, Field
from typing import Optional

from states.schemas.intent import UserIntentModel
from states.schemas.research import ResearchOutputModel
from states.schemas.planner import ItineraryModel
from states.schemas.pricing import PricingModel

# Model : Final, user-approved trip plan (for debugging / storage)
class FinalTripPlanModel(BaseModel):
    
    user_intent: UserIntentModel = Field(
        description="Normalized user requirements"
    )

    research_summary: ResearchOutputModel = Field(
        description="Approved research findings"
    )

    itinerary: ItineraryModel = Field(
        description="Approved day-by-day plan"
    )

    pricing: PricingModel = Field(
        description="Final cost breakdown and risks"
    )

    notes: Optional[str] = Field(
        default=None,
        description="Optional system notes or disclaimers"
    )