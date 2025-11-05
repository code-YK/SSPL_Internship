from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from db.database import Base

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)

    def __init__(self, name: str, start_date: Date, end_date: Date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date