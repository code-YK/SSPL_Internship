from sqlalchemy import Column, DateTime, Integer, String, Boolean
from config.db_config import Base
from sqlalchemy.orm import relationship

class Depot(Base):
    __tablename__ = 'depots'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    address = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False) 

    # Relationships (1 to Many)
    drivers = relationship("Driver", back_populates="depot")
    packages = relationship("Package", back_populates="depot")
