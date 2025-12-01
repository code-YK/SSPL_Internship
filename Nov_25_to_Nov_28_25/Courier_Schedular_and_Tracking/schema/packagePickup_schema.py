from pydantic import BaseModel, Field
from .package_schema import PackageCreate
from .pickup_request_schema import PickupRequestCreate

class PackagePickupCreate(BaseModel):
    package: PackageCreate
    pickupinfo: PickupRequestCreate

    class Config:
        from_attributes = True
