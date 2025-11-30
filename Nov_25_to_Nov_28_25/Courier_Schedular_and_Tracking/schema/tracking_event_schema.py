from pydantic import BaseModel, Field
from pydantic.datetime_parse import datetime

class TrackingEventCreate(BaseModel):
    package_id: int = Field(..., alias="package_id")
    event_time: datetime = Field(..., alias="event_time")
    location: str = Field(..., alias="location")
    description: str = Field(..., alias="description")

    class Config:
        orm_mode = True

class TrackingEventRead(TrackingEventCreate):
    id: int = Field(..., alias="id")