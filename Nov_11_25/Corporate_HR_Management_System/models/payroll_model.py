from sqlalchemy import Column, Enum, Float, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from config.db import Base
from config.enum import PayrollStatusEnum

class Payroll(Base):
    __tablename__ = 'payrolls'

    payroll_id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'), nullable=False)
    base_salary = Column(Integer, nullable=False)
    allowances = Column(Float, nullable=False)
    deductions = Column(Float, nullable=False)
    net_pay = Column(Float, nullable=False)
    status = Column(Enum(PayrollStatusEnum), default=PayrollStatusEnum.pending, nullable=False)
    pay_date = Column(Date, nullable=False)

    employee = relationship("Employee", back_populates="payrolls")