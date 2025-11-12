from pydantic import BaseModel, Field, EmailStr
from datetime import date
from config.enum import GenderEnum

class EmployeeBase(BaseModel):
    name : str = Field(..., min_length=3, max_length=100)
    email : EmailStr = Field(..., description="Email must be a valid email address")
    gender : GenderEnum
    hire_date : date = Field(..., description="Hire date in YYYY-MM-DD format")
    salary : int = Field(..., gt=0, description="Salary must be a positive integer")

    class Config:
        from_attributes = True  # Enable ORM mode to work with SQLAlchemy models

class EmployeeCreate(EmployeeBase):
    dept_id : int = Field(..., gt=0, description="It must be a valid department ID")

class EmployeeRead(EmployeeBase):
    emp_id : int
    dept_id : int | None = None

class EmployeeUpdate(BaseModel):
    name : str | None = Field(None, min_length=3, max_length=100)
    email : EmailStr | None = Field(None, description="Email must be a valid email address")
    gender : GenderEnum | None = None
    hire_date : date | None = Field(None, description="Hire date in YYYY-MM-DD format")
    dept_id : int | None = Field(None, gt=0, description="It must be a valid department ID")
    salary : int | None = Field(None, gt=0, description="Salary must be a positive integer")
    
    