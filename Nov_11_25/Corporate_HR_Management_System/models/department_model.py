from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from models.employee_model import Employee

class Department(Base):
    __tablename__ = 'departments'

    dept_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    manager_id = Column(Integer, ForeignKey('employees.emp_id'), nullable=False)
    budget = Column(Float, nullable=False)

    manager = relationship(
        "Employee",
        foreign_keys=[manager_id]
    )

    employees = relationship(
        "Employee",
        foreign_keys=[Employee.dept_id],
        back_populates="department"
    )