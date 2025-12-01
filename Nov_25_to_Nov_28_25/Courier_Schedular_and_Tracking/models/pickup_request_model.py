from sqlalchemy import Column, DateTime, Enum, Integer, String, ForeignKey
from config import Base, pickupStatus
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class PickupRequest(Base):
    __tablename__ = 'pickup_requests'

    id = Column(Integer, primary_key=True, index=True)
    package_id = Column(Integer, ForeignKey('packages.id'), nullable=False)
    requested_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))
    scheduled_at = Column(DateTime, nullable=True)
    driver_id = Column(Integer, ForeignKey('drivers.id'), nullable=True)
    status = Column(Enum(pickupStatus), default=pickupStatus.PENDING, nullable=False)

    # Relationships (1 to 1)
    package = relationship("Package", uselist=False, back_populates="pickup_request")

    # Relationships (Many to 1)
    driver = relationship("Driver", back_populates="pickup_requests")

    