from pydantic import BaseModel, Field
from datetime import datetime
from config import packageStatus

class PackageCreate(BaseModel):
    recipient_name: str
    address: str
    status: packageStatus = packageStatus.CREATED
    tracking_number: str

    class Config:
        from_attributes = True


class PackageRead(PackageCreate):
    id: int
    depot_id: int
    created_at: datetime
    updated_at: datetime