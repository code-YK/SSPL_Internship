from pydantic import BaseModel, Field
from datetime import date
from config.enum import LeaveStatusEnum, LeaveTypeEnum

class LeaveRecordBase(BaseModel):
    start_date: date = Field(..., description="The start date of the leave")
    end_date: date = Field(..., gt=start_date, description="The end date of the leave")
    reason: str = Field(..., description="The reason for the leave")
    status: LeaveStatusEnum = Field(LeaveStatusEnum.pending, description="The status of the leave request (pending, approved, rejected)")
    leave_type: LeaveTypeEnum = Field(LeaveTypeEnum.sick, description="The type of leave (casual, sick, annual, unpaid)")

    class Config:
        orm_mode = True

class LeaveRecordCreate(LeaveRecordBase):
    emp_id: int = Field(..., description="The ID of the employee requesting leave")
    approved_by: int | None = Field(None, description="The ID of the approver, if applicable")

class LeaveRecordRead(LeaveRecordBase):
    leave_id: int
    emp_id: int
    approved_by: int | None = None

