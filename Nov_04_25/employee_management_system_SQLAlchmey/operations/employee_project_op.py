from datetime import date
from sqlalchemy.exc import SQLAlchemyError
from models import EmployeeProject

# assign an employee to a project
def assign_employee_to_project(session, emp_id: int, project_id: int, assigned_date: date):
    try:
        new_assignment = EmployeeProject(emp_id=emp_id, project_id=project_id, assigned_date=assigned_date)
        session.add(new_assignment)
        session.commit()
        print(f"Assigned Employee ID {emp_id} to Project ID {project_id} on {assigned_date}")
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    
