from pydantic import BaseModel, Field
from datetime import date
from config.enum import PayrollStatusEnum

class PayrollBase(BaseModel):
    base_salary : int = Field(..., gt=0, description="Base salary must be same as in employee record")
    allowances : float = Field(..., ge=0, description="Allowances must be a non-negative number") 
    deductions : float = Field(..., ge=0, description="Deductions must be a non-negative number")
    net_pay : float = Field(..., gt=0, description="Net pay must be a positive number")
    status : PayrollStatusEnum = Field(..., description="Status of the payroll(pending, paid)")
    pay_date : date = Field(..., description="Pay date")

    class Config:
        from_attributes = True

class PayrollCreate(PayrollBase):
    emp_id : int = Field(..., description="The ID must refer to a valid employee")

class PayrollRead(PayrollBase):
    payroll_id : int
    emp_id : int
