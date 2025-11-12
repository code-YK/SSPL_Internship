from crud import  view_all_payrolls, get_payroll_by_emp_id, update_payroll_status, generate_payroll_for_employee
from config.db import SessionLocal
from config.enum import PayrollStatusEnum
from datetime import date
from config.logger_config import setup_logger

logger = setup_logger(__name__)

def payroll_menu():
    db = SessionLocal()
        
    while True:
        print("====Payroll Management Menu:====")
        print("1. View All Payroll Records")
        print("2. View Payroll by Employee ID")
        print("3. Update Payroll Status")
        print("4. Generate Payroll for Employee")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            try:
                view_all_payrolls(db)
            except Exception as e:
                logger.error(f"Error viewing all payrolls: {e}")
                raise

        elif choice == '2':
            try:
                emp_id = int(input("Enter employee ID: "))
                get_payroll_by_emp_id(db, emp_id)
            except Exception as e:
                logger.error(f"Error retrieving payroll by employee ID: {e}")
                raise

        elif choice == '3':
            payroll_id = int(input("Enter payroll ID to update: "))
            new_status = input("Enter new status (pending/paid): ").lower()
            update_payroll_status(db, payroll_id, PayrollStatusEnum(new_status))

        elif choice == '4':
            emp_id = int(input("Enter employee ID to generate payroll for: "))
            pay_date = input("Enter pay date (YYYY-MM-DD): ")
            generate_payroll_for_employee(db, emp_id, date.fromisoformat(pay_date))

        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")

    db.close()
