from typing import TypedDict, List, Optional
from typing_extensions import Annotated

from langchain_core.messages import BaseMessage

from utils import rolling_message_reducer as add_messages

from states.schemas import *

class TripEventState(TypedDict, total=False):

    # Conversation Memory
    messages: Annotated[List[BaseMessage], add_messages]

    # User Intent
    user_intent: Optional[UserIntentModel]

    # Research Stage
    research_result: Optional[ResearchOutputModel]
    research_review: Optional[ReviewDecisionModel]

    # Planning Stage
    itinerary: Optional[ItineraryModel]
    planner_review: Optional[ReviewDecisionModel]

    # Pricing Stage
    pricing: Optional[PricingModel]
    pricing_review: Optional[ReviewDecisionModel]

    # Control Flags
    current_stage: Optional[str]
    final_approved: bool
    final_trip_plan: Optional[FinalTripPlanModel]