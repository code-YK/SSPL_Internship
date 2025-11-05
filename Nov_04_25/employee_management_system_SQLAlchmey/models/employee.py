from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from db.database import Base

class Employee(Base):
    __tablename__ = "employees"

    emp_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    salary = Column(Integer)
    hire_date = Column(Date)
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))
    department = relationship("Department", back_populates="employees")

    def __init__(self, name: str, salary: int, hire_date: Date, dept_id: int):
        self.name = name
        self.salary = salary
        self.hire_date = hire_date
        self.dept_id = dept_id
    
    