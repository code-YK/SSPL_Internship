from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from config import Base
from sqlalchemy.orm import relationship

class TrackingEvent(Base):
    __tablename__ = 'tracking_events'

    id = Column(Integer, primary_key=True, index=True)
    package_id = Column(Integer, ForeignKey('packages.id'), nullable=False)
    event_time = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # Relationships (Many to 1)
    package = relationship("Package", back_populates="tracking_events")
    