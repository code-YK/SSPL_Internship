from pydantic import BaseModel, Field
from pydantic.datetime_parse import datetime

class DepotCreate(BaseModel):
    name: str = Field(..., alias="name")
    address: str = Field(..., alias="address")
    is_active: bool = Field(..., alias="is_active")

    class Config:
        orm_mode = True

class DepotRead(DepotCreate):
    id: int = Field(..., alias="id")
    created_at: datetime = Field(..., alias="created_at")