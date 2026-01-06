from pydantic import BaseModel, Field
from typing import Optional

# Model : Review decision by user (Human-In-The-Loop)
class ReviewDecisionModel(BaseModel):
    approved: bool = Field(
        description="Whether the user approves the current stage"
    )
    feedback: Optional[str] = Field(
        default=None, description="User feedback or requested changes"
    )
    revision_target: Optional[str] = Field(
        default=None,
        description="research / planner / pricing (if changes needed)"
    )
