from pydantic import BaseModel, Field
from datetime import datetime

class DepotCreate(BaseModel):
    name: str = Field(..., alias="name")
    address: str = Field(..., alias="address")
    is_active: bool = Field(..., alias="is_active")

    class Config:
        from_attributes = True

class DepotRead(DepotCreate):
    id: int = Field(..., alias="id")
    created_at: datetime = Field(..., alias="created_at")