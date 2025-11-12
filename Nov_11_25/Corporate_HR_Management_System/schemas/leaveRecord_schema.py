from typing import Self
from pydantic import BaseModel, Field, model_validator
from datetime import date
from config.enum import LeaveStatusEnum, LeaveTypeEnum

class LeaveRecordBase(BaseModel):
    start_date: date = Field(..., description="The start date of the leave")
    end_date: date = Field(..., description="The end date of the leave")
    reason: str = Field(..., description="The reason for the leave")
    leave_type: LeaveTypeEnum = Field(LeaveTypeEnum.sick, description="The type of leave (casual, sick, annual, unpaid)")

    @model_validator(mode="after")
    def check_dates(self) -> Self:
        # Validate that end_date occurs after start_date.
        if self.end_date <= self.start_date:
            raise ValueError("end_date must be after start_date")
        return self
    
    class Config:
        from_attributes = True

class LeaveRecordCreate(LeaveRecordBase):
    emp_id: int = Field(..., description="The ID of the employee requesting leave")
    approved_by: int | None = Field(None, description="The ID of the approver, if applicable")

class LeaveRecordRead(LeaveRecordBase):
    leave_id: int
    emp_id: int
    approved_by: int | None = None

