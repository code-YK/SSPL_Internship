from enum import Enum

class packageStatus(Enum):
    CREATED = "created"
    IN_TRANSIT = "in transit"
    DELIVERED = "delivered"

class pickupStatus(Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    PENDING = "pending"