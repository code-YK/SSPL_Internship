# This file contains enumerations used across the task

from enum import Enum

class GenderEnum(Enum):
    male = "male"
    female = "female"

class LeaveStatusEnum(Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class LeaveTypeEnum(Enum):
    casual = "casual"
    sick = "sick"
    unpaid = "unpaid"
    annual = "annual"

class PayrollStatusEnum(Enum):
    pending = "pending"
    paid = "paid"