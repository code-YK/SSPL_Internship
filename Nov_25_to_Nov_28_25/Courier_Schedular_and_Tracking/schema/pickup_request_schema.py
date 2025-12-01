from pydantic import BaseModel, Field
from datetime import datetime
from config import pickupStatus

class PickupRequestCreate(BaseModel):
    driver_id: int
    scheduled_at: datetime

    class Config:
        from_attributes = True

class PickupRequestRead(PickupRequestCreate):
    id: int
    package_id: int
    requested_at: datetime
    status: pickupStatus