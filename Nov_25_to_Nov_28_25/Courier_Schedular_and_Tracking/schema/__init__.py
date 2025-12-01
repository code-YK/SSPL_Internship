from .depot_schema import DepotCreate, DepotRead
from .driver_schema import DriverCreate, DriverRead
from .package_schema import PackageCreate, PackageRead
from .pickup_request_schema import PickupRequestCreate, PickupRequestRead
from .tracking_event_schema import TrackingEventCreate, TrackingEventRead
from .packagePickup_schema import PackagePickupCreate

__all__ = [
    'DepotCreate',
    'DepotRead',
    'DriverCreate',
    'DriverRead',
    'PackageCreate',
    'PackageRead',
    'PickupRequestCreate',
    'PickupRequestRead',
    'TrackingEventCreate',
    'TrackingEventRead',
    'PackagePickupCreate'
]
