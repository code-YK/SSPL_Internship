from operations import assign_employee_to_project, add_project, view_all_projects, view_ongoing_projects, add_employee, view_all_employees, delete_employee, increment_employee_salary, add_department, view_all_departments
from db import SessionLocal

session = SessionLocal()

def display_menu():
    while True:
        print("\nEmployee Management System Menu:")
        print("1. Add Department")
        print("2. Add Employee")
        print("3. Add Project")
        print("4. Assign Employee to Project")
        print("5. View Departments")
        print("6. View Employees")
        print("7. View All Projects")
        print("8. View all Ongoing Projects")
        print("9. Increase Employee Salary")
        print("10. Delete Employee")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")
        
        if choice == '1':
            name = input("Enter Department Name: ")
            location = input("Enter Department Location: ")
            add_department(session, name, location)
        
        elif choice == '2':
            name = input("Enter Employee Name: ")
            salary = int(input("Enter Employee Salary: "))
            hire_date = input("Enter Hire Date (YYYY-MM-DD): ")
            dept_id = int(input("Enter Department ID: "))
            add_employee(session, name, salary, hire_date, dept_id)

        elif choice == '3':
            name = input("Enter Project Name: ")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD) or leave blank if ongoing: ")
            end_date = end_date if end_date else None
            add_project(session, name, start_date, end_date)
        
        elif choice == '4':
            emp_id = int(input("Enter Employee ID: "))
            project_id = int(input("Enter Project ID: "))
            assign_employee_to_project(session, emp_id, project_id)

        elif choice == '5':
            view_all_departments(session)

        elif choice == '6':
            view_all_employees(session)
        
        elif choice == '7':
            view_all_projects(session)

        elif choice == '8':
            view_ongoing_projects(session)

        elif choice == '9':
            emp_id = int(input("Enter Employee ID: "))
            percent = float(input("Enter Salary Increment Percentage: "))
            increment_employee_salary(session, emp_id, percent)

        elif choice == '10':
            emp_id = int(input("Enter Employee ID to Delete: "))
            delete_employee(session, emp_id)
        
        elif choice == '11':
            session.close()
            print("Exiting Employee Management System.")
            break
