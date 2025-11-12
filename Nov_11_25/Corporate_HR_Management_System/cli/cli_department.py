from crud import add_department, view_all_departments
from schemas import DepartmentCreate
from config.db import SessionLocal
from config.logger_config import setup_logger

logger = setup_logger(__name__)

def department_menu():
    db = SessionLocal()

    while True:
        print("====Department Management Menu:====")
        print("1. Add New Department")
        print("2. View All Departments")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                name = input("Enter department name: ")
                budget = float(input("Enter department budget: "))
                manager_id = int(input("Enter manager employee ID: "))

                dept_data = DepartmentCreate(
                    name=name,
                    budget=budget,
                    manager_id=manager_id
                )

                dept = add_department(db, dept_data)
            except Exception as e:
                logger.error(f"Error adding department: {e}")
                raise

        elif choice == '2':
            view_all_departments(db)

        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please try again.")
            
    db.close()