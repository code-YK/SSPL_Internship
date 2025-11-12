# This file contains enumerations used across the task

from enum import Enum

class GenderEnum(Enum):
    male = "Male"
    female = "Female"

class LeaveStatusEnum(Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"

class LeaveTypeEnum(Enum):
    casual = "Casual"
    sick = "Sick"
    unpaid = "Unpaid"
    annual = "Annual"

class PayrollStatusEnum(Enum):
    pending = "Pending"
    paid = "Paid"