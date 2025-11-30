from pydantic import BaseModel, Field
from pydantic.datetime_parse import datetime
from config import packageStatus

class PackageCreate(BaseModel):
    recipent_name: str = Field(..., alias="recipient_name")
    address: str = Field(..., alias="address")
    depot_id: int = Field(..., alias="depot_id")
    status: packageStatus = Field(packageStatus.CREATED, alias="status")
    created_at: datetime = Field(..., alias="created_at")
    updated_at: datetime = Field(..., alias="updated_at")
    tracking_number: str = Field(..., alias="tracking_number")

    class Config:
        orm_mode = True

class PackageRead(PackageCreate):
    id: int = Field(..., alias="id")
    