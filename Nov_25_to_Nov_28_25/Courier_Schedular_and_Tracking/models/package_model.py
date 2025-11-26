from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Enum
from config import Base, packageStatus
from sqlalchemy.orm import relationship


class Package(Base):
    __tablename__ = 'packages'

    id = Column(Integer, primary_key=True, index=True)
    recipent_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    depot_id = Column(Integer, ForeignKey('depots.id'))
    tracking_id = Column(Integer, ForeignKey('trackings.id'), nullable=True)
    status = Column(Enum(packageStatus), default=packageStatus.CREATED, nullable=False)
    
    # Relationships (1 to Many)
    depot = relationship("Depot", back_populates="packages")
    tracking = relationship("Tracking", back_populates="packages")
