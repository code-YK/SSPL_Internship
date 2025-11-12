from sqlalchemy import Column, Enum, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from config.db import Base
from config.enum import GenderEnum

class Employee(Base):
    __tablename__ = 'employees'

    emp_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    gender = Column(Enum(GenderEnum), nullable=False)
    hire_date = Column(Date, nullable=False)
    dept_id = Column(Integer, ForeignKey('departments.dept_id'))
    salary = Column(Integer, nullable=False)

    department = relationship(
            "Department",
            back_populates="employees",
            foreign_keys=[dept_id]
        )

    payrolls = relationship("Payroll", back_populates="employee")

    leave_records = relationship(
        "LeaveRecord",
        back_populates="employee",
        foreign_keys="LeaveRecord.emp_id"
    )

    approved_leaves = relationship(
        "LeaveRecord",
        foreign_keys="LeaveRecord.approved_by",
        backref="approver"
    )