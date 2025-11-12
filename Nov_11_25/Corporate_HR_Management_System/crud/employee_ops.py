from sqlalchemy.orm import Session
from models import Employee, Department
from schemas import EmployeeCreate, EmployeeUpdate
from config.logger_config import setup_logger
from typing import Optional
import tabulate

logger = setup_logger(__name__)

# add new employee
def add_employee(db: Session, employee_data: EmployeeCreate) -> Employee:

    # Check if department exists
    department = db.query(Department).filter(Department.dept_id == employee_data.dept_id).first()
    if not department:
        logger.error(f"Department with id {employee_data.dept_id} does not exist.")
        raise ValueError(f"Department with id {employee_data.dept_id} does not exist.")

    # Check if email is already used
    existing_employee = db.query(Employee).filter(Employee.email == employee_data.email).first()
    if existing_employee:
        logger.error(f"Email {employee_data.email} is already in use.")
        raise ValueError(f"Email {employee_data.email} is already in use.")
    
    new_employee = Employee(
        name=employee_data.name,
        email=employee_data.email,
        dept_id=employee_data.dept_id,
        gender=employee_data.gender,
        hire_date=employee_data.hire_date,
        salary=employee_data.salary
    )

    try:
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        logger.info(f"Added new employee with id {new_employee.emp_id}.")
        return new_employee
    except Exception as e:
        logger.error(f"Error adding new employee: {e}")
        db.rollback()
        raise
    finally:
        db.close()

    
# get employee by id
def get_employee(db: Session, emp_id: int) -> Optional[Employee]:
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        logger.warning(f"Employee with id {emp_id} not found.")
    return employee

# update employee details
def update_employee(db: Session, emp_id: int, update_data: EmployeeUpdate) -> Optional[Employee]:
    employee = get_employee(db, emp_id)  # Check if employee exists

    if not employee:
        logger.error(f"Employee with id {emp_id} not found.")
        return None
    try: 
        # Update fields
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(employee, field, value)

        db.commit()
        db.refresh(employee)
        logger.info(f"Updated employee with id {emp_id}.")
        return employee
    except Exception as e:
        logger.error(f"Error updating employee with id {emp_id}: {e}")
        db.rollback()
        raise
    finally:
        db.close()


def delete_employee(db: Session, emp_id: int) -> bool:
    employee = get_employee(db, emp_id)  # Check if employee exists
    if not employee:
        logger.error(f"Employee with id {emp_id} not found.")
        return False
    
    try:
        db.delete(employee)
        db.commit()
        logger.info(f"Deleted employee with id {emp_id}.")
        return True
    except Exception as e:
        logger.error(f"Error deleting employee with id {emp_id}: {e}")
        db.rollback()
        return False
    finally:
        db.close()

def view_all_employees(db: Session) -> None:
    employees = db.query(Employee).all()
    if not employees:
        logger.info("No employees found.")
        return

    employee_data = [
        {
            "ID": emp.emp_id,
            "Name": emp.name,
            "Email": emp.email,
            "Department ID": emp.dept_id,
            "Gender": emp.gender.value,
            "Hire Date": emp.hire_date,
            "Salary": emp.salary
        }
        for emp in employees
    ]
    logger.info("Employees retrieved successfully.")
    print(tabulate.tabulate(employee_data, headers="keys", tablefmt="grid"))
    logger.info(f"Displayed {len(employees)} employees.")
