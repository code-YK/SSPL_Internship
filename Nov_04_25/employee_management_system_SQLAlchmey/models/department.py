from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from db.database import Base

class Department(Base):
    __tablename__ = "departments"

    dept_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)
    employees = relationship("Employee", back_populates="department")

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

    