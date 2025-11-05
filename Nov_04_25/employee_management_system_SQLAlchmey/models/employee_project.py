from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from db.database import Base

class EmployeeProject(Base):
    __tablename__ = "employee_projects"

    emp_proj_id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(Integer, ForeignKey("employees.emp_id"))
    project_id = Column(Integer, ForeignKey("projects.project_id"))
    assigned_date = Column(Date)

    employee = relationship("Employee", backref="employee_projects")
    project = relationship("Project", backref="employee_projects")

    def __init__(self, emp_id: int, project_id: int, assigned_date: Date):
        self.emp_id = emp_id
        self.project_id = project_id
        self.assigned_date = assigned_date  