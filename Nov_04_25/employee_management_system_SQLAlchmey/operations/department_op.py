from datetime import date
from sqlalchemy.exc import SQLAlchemyError
from models import Department

# add a new department
def add_department(session, name: str, location: str):
    try:
        new_department = Department(name=name, location=location)
        session.add(new_department)
        session.commit()
        print(f"Added department: {new_department.name} with ID {new_department.dept_id}")
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    

# View all departments
def view_all_departments(session):
    try:
        departments = session.query(Department).all()
        for dept in departments:
            print(f"""
                  ID: {dept.dept_id}, 
                  Name: {dept.name}, 
                  Location: {dept.location}
                -------------------------------""")
    except SQLAlchemyError as e:
        raise e
    
    