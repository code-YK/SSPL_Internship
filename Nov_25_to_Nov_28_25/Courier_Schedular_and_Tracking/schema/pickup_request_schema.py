from pydantic import BaseModel, Field
from pydantic.datetime_parse import datetime
from config import pickupStatus

class PickupRequestCreate(BaseModel):
    package_id : int = Field(..., alias="package_id")
    driver_id : int = Field(..., alias="driver_id")
    requested_at : datetime = Field(..., alias="requested_at")
    scheduled_at : datetime = Field(None, alias="scheduled_at")
    status : pickupStatus = Field(pickupStatus.PENDING, alias="status")
    
    class Config:
        orm_mode = True

class PickupRequestRead(PickupRequestCreate):
    id : int = Field(..., alias="id")