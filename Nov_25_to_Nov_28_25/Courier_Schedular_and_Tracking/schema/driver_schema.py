from pydantic import BaseModel, Field

class DriverCreate(BaseModel):
    name: str = Field(..., alias="name")
    phone : str = Field(..., alias="phone")
    depot_id: int = Field(..., alias="depot_id")
    is_active: bool = Field(True, alias="is_active")

    class Config:
        from_attributes = True

class DriverRead(DriverCreate):
    id: int = Field(..., alias="id")

