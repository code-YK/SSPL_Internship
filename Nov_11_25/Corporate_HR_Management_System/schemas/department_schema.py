from pydantic import BaseModel, Field

class DepartmentBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100)
    budget: float = Field(..., gt=0, description="Budget must be a positive number")

    class Config:
        from_attributes = True # Enable ORM mode to work with SQLAlchemy models

class DepartmentCreate(DepartmentBase):
    manager_id: int = Field(..., gt=0, description="Manager ID must be a valid employee ID")

class DepartmentRead(DepartmentBase):
    dept_id: int
    manager_id: int

