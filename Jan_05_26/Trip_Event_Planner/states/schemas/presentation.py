from pydantic import BaseModel, Field

# Model : User-friendly trip plan summary
# only used if pricing approved by user
class UserFriendlyTripPlan(BaseModel):
    title: str = Field(
        description="Short title for the trip plan"
    )

    summary: str = Field(
        description="High-level overview of the trip and event"
    )

    itinerary_overview: str = Field(
        description="Day-by-day plan written in simple language"
    )

    budget_summary: str = Field(
        description="Easy-to-understand cost explanation"
    )

    highlights: str = Field(
        description="Key highlights and special moments"
    )

    important_notes: str = Field(
        description="Things the user should be aware of"
    )
