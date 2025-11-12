from crud import view_all_employees, add_employee, get_employee, update_employee, delete_employee
from config.db import SessionLocal
from config.enum import GenderEnum
from datetime import date
from tabulate import tabulate
from schemas import EmployeeCreate, EmployeeUpdate
from config.logger_config import setup_logger

logger = setup_logger(__name__)

def employee_menu():
    
    db = SessionLocal()
        
    while True:
        print("====Employee Management Menu:====")
        print("1. Add New Employee")
        print("2. View All Employee Details")
        print("3. Update Employee Details")
        print("4. Delete Employee")
        print("5. View Employees by ID")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            try:
                name = input("Enter name: ")
                email = input("Enter email: ")
                gender = input("Enter gender (male/female): ").lower()
                hire_date = input("Enter hire date (YYYY-MM-DD): ")
                dept_id = int(input("Enter department ID: "))
                salary = int(input("Enter salary: "))

                emp_data = EmployeeCreate(
                    name=name,
                    email=email,
                    gender=GenderEnum(gender),
                    hire_date=date.fromisoformat(hire_date),
                    dept_id=dept_id,
                    salary=salary
                )

                emp = add_employee(db, emp_data)
            except Exception as e:
                logger.error(f"Error adding employee: {e}")
                raise

        elif choice == '2':
            view_all_employees(db)
        
        elif choice == '3':
            try:
                emp_id = int(input("Enter employee ID to update: "))

                # Build update data only with non-empty values
                update_data = {}

                name = input("Enter new name (leave blank to keep current): ").strip()
                if name:
                    update_data["name"] = name

                email = input("Enter new email (leave blank to keep current): ").strip()
                if email:
                    update_data["email"] = email

                gender = input("Enter new gender (M/F, leave blank to keep current): ").strip().lower()
                if gender:
                    update_data["gender"] = GenderEnum(gender)

                hire_date = input("Enter new hire date (YYYY-MM-DD, leave blank to keep current): ").strip()
                if hire_date:
                    update_data["hire_date"] = date.fromisoformat(hire_date)

                dept_id = input("Enter new department ID (leave blank to keep current): ").strip()
                if dept_id:
                    update_data["dept_id"] = int(dept_id)

                salary = input("Enter new salary (leave blank to keep current): ").strip()
                if salary:
                    update_data["salary"] = int(salary)

                emp_data = EmployeeUpdate(**update_data)

                emp = update_employee(db, emp_id, emp_data)
            except Exception as e:
                logger.error(f"Error updating employee: {e}")
                raise

        elif choice == '4':
            emp_id = int(input("Enter employee ID to delete: "))
            delete_employee(db, emp_id)


        elif choice == '5':
            emp_id = int(input("Enter employee ID to view: "))
            emp = get_employee(db, emp_id)
            if emp:
                emp_data = [{
                    "emp_id": emp.emp_id,
                    "name": emp.name,
                    "email": emp.email,
                    "gender": emp.gender.name,
                    "hire_date": emp.hire_date,
                    "dept_id": emp.dept_id,
                    "salary": emp.salary
                }]
                print(tabulate(emp_data, headers="keys", tablefmt="grid"))
            else:
                logger.info(f"Employee with id {emp_id} not found.")

        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Please try again.")

    db.close()