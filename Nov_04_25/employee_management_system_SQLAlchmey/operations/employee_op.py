from datetime import date
from sqlalchemy.exc import SQLAlchemyError
from models import Employee

# add a new employee
def add_employee(session, name: str, salary: int, hire_date: date, dept_id: int):
    try:
        new_employee = Employee(name=name, salary=salary, hire_date=hire_date, dept_id=dept_id)
        session.add(new_employee)
        session.commit()
        print(f"Added employee: {new_employee.name} with ID {new_employee.emp_id}")
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    
# delete an employee by ID
def delete_employee(session, emp_id: int):
    try:
        employee = session.query(Employee).filter(Employee.emp_id == emp_id).first()
        if employee:
            session.delete(employee)
            session.commit()
            print(f"Deleted employee with ID {emp_id}")
        else:
            print(f"No employee found with ID {emp_id}")
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    
# view all employees
def view_all_employees(session):
    try:
        employees = session.query(Employee).all()
        for emp in employees:
            print(f"""
                  ID: {emp.emp_id}, 
                  Name: {emp.name}, 
                  Salary: {emp.salary}, 
                  Hire Date: {emp.hire_date}, 
                  Dept ID: {emp.dept_id}
                -------------------------------""")
    except SQLAlchemyError as e:
        raise e
    
# Salary increment for an employee
def increment_employee_salary(session, emp_id: int, percent: float):
    try:
        employee = session.query(Employee).filter(Employee.emp_id == emp_id).first()
        if employee:
            increment_amount = employee.salary * (percent / 100)
            employee.salary += increment_amount
            session.commit()
            print(f"Incremented salary of Employee ID {emp_id} by {increment_amount}. New Salary: {employee.salary}")
        else:
            print(f"No employee found with ID {emp_id}")
    except SQLAlchemyError as e:
        session.rollback()
        raise e