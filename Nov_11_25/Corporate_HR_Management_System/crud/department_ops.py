from sqlalchemy.orm import Session
from models import Department, Employee
from schemas import DepartmentCreate
from config.logger_config import setup_logger
import tabulate

logger = setup_logger(__name__)

# add new department
def add_department(db: Session, department_data: DepartmentCreate) -> Department:

    # Check if manager exists
    manager = db.query(Employee).filter(Employee.emp_id == department_data.manager_id).first()
    if not manager:
        logger.error(f"Employee with id {department_data.manager_id} does not exist.")
        raise ValueError(f"Employee with id {department_data.manager_id} does not exist.")

    new_department = Department(
        name=department_data.name,
        budget=department_data.budget,
        manager_id=department_data.manager_id
    )

    try:
        db.add(new_department)
        db.commit()
        db.refresh(new_department)
        logger.info(f"Added new department with id {new_department.dept_id}.")
        return new_department
    except Exception as e:
        logger.error(f"Error adding new department: {e}")
        db.rollback()
        raise
    finally:
        db.close()


# View all departments
def view_all_departments(db: Session) -> None:
    departments = db.query(Department).all()
    if not departments:
        logger.info("No departments found.")
        return []

    dept_list = [{
        "dept_id": dept.dept_id,
        "name": dept.name,
        "budget": dept.budget,
        "manager_id": dept.manager_id
    } for dept in departments]

    logger.info("Departments retrieved successfully.")
    print(tabulate.tabulate(dept_list, headers="keys", tablefmt="grid"))
    logger.info(f"Displayed {len(dept_list)} departments.")

