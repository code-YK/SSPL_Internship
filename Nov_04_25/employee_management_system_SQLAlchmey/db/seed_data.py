from datetime import date
from db.database import SessionLocal, engine, Base
from models import Department, Employee, Project, EmployeeProject

# Create all tables
Base.metadata.create_all(bind=engine)

# Start a session
session = SessionLocal()

# Departments
departments = [
    Department(name="Human Resources", location="Mumbai"),
    Department(name="Information Technology", location="Bengaluru"),
    Department(name="Finance", location="Delhi"),
    Department(name="Marketing", location="Pune"),
    Department(name="Operations", location="Hyderabad")
]

session.add_all(departments)
session.commit()

# Employees
employees = [
    Employee(name="Rohan Mehta", salary=85000, hire_date=date(2020, 6, 12), dept_id=2),
    Employee(name="Priya Sharma", salary=55000, hire_date=date(2019, 3, 21), dept_id=1),
    Employee(name="Amit Verma", salary=72000, hire_date=date(2021, 7, 10), dept_id=3),
    Employee(name="Sneha Iyer", salary=60000, hire_date=date(2022, 1, 15), dept_id=4),
    Employee(name="Rahul Khanna", salary=65000, hire_date=date(2018, 9, 23), dept_id=5),
    Employee(name="Karan Gupta", salary=95000, hire_date=date(2019, 5, 30), dept_id=2),
    Employee(name="Divya Nair", salary=48000, hire_date=date(2023, 2, 12), dept_id=1),
    Employee(name="Arjun Singh", salary=105000, hire_date=date(2021, 8, 19), dept_id=2),
    Employee(name="Meena Reddy", salary=70000, hire_date=date(2019, 12, 2), dept_id=3),
    Employee(name="Tanya Kapoor", salary=59000, hire_date=date(2021, 9, 27), dept_id=4),
]

session.add_all(employees)
session.commit()

# Projects
projects = [
    Project(name="AI Chatbot Integration", start_date=date(2023, 1, 10), end_date=date(2023, 10, 20)),
    Project(name="Payroll Automation", start_date=date(2022, 3, 15), end_date=date(2022, 11, 30)),
    Project(name="Digital Marketing Revamp", start_date=date(2023, 6, 5), end_date=None),
    Project(name="Inventory Optimization", start_date=date(2021, 7, 1), end_date=date(2022, 5, 15)),
    Project(name="Data Security Upgrade", start_date=date(2023, 8, 1), end_date=None)
]

session.add_all(projects)
session.commit()

# Employee–Project Assignments
employee_projects = [
    EmployeeProject(emp_id=1, project_id=1, assigned_date=date(2023, 1, 15)),
    EmployeeProject(emp_id=2, project_id=2, assigned_date=date(2022, 4, 10)),
    EmployeeProject(emp_id=3, project_id=5, assigned_date=date(2023, 8, 5)),
    EmployeeProject(emp_id=4, project_id=3, assigned_date=date(2023, 6, 10)),
    EmployeeProject(emp_id=5, project_id=4, assigned_date=date(2021, 7, 10)),
    EmployeeProject(emp_id=6, project_id=1, assigned_date=date(2023, 2, 5)),
    EmployeeProject(emp_id=7, project_id=3, assigned_date=date(2023, 6, 20)),
    EmployeeProject(emp_id=8, project_id=5, assigned_date=date(2023, 8, 10)),
    EmployeeProject(emp_id=9, project_id=2, assigned_date=date(2022, 5, 25)),
    EmployeeProject(emp_id=10, project_id=4, assigned_date=date(2021, 8, 1)),
]

session.add_all(employee_projects)
session.commit()

print("Database seeded successfully with sample data!")
session.close()
