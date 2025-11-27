from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from config.db_config import Base
from sqlalchemy.orm import relationship

class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    depot_id = Column(Integer, ForeignKey('depots.id'))

    # Relationships (1 to Many)
    depot = relationship("Depot", back_populates="drivers")
    pickup_requests = relationship("PickupRequest", back_populates="driver")