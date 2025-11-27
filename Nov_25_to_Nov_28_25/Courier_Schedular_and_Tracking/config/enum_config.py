from enum import Enum

class packageStatus(Enum):
    CREATED = "created"
    IN_TRANSIT = "in transit"
    DELIVERED = "delivered"
    PENDING = "pending"
    SHIPPED = "shipped"
    OUT_FOR_DELIVERY = "out for delivery"
    CANCELLED = "cancelled"

class pickupStatus(Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    PENDING = "pending"