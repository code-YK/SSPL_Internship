from sqlalchemy import Column, Enum, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from config.db import Base
from config.enum import LeaveStatusEnum, LeaveTypeEnum

class LeaveRecord(Base):
    __tablename__ = 'leave_records'

    leave_id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    reason = Column(String, nullable=False)
    status = Column(Enum(LeaveStatusEnum), default=LeaveStatusEnum.pending, nullable=False)
    leave_type = Column(Enum(LeaveTypeEnum), default=LeaveTypeEnum.sick, nullable=False)
    approved_by = Column(Integer, ForeignKey('employees.emp_id'), nullable=True)

    # Relationships
    employee = relationship(
        "Employee",
        back_populates="leave_records",
        foreign_keys=[emp_id]  # specify foreign key for employee
    )
