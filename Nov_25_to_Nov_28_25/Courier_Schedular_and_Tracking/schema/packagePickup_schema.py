from pydantic import BaseModel, Field
from .package_schema import PackageCreate
from .pickup_request_schema import PickupRequestRead

class PackagePickupCreate(BaseModel):
    package: PackageCreate = Field(..., alias="package")
    pickupinfo: PickupRequestRead = Field(..., alias="pickupinfo")

    class Config:
        orm_mode = True
        