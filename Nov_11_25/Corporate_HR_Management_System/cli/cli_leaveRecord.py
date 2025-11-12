from crud import add_leave_record, view_all_leave_records, view_leave_records_by_employee, update_leave_record_status
from config.db import SessionLocal
from config.logger_config import setup_logger
from config.enum import LeaveTypeEnum, LeaveStatusEnum
from schemas import LeaveRecordCreate

logger = setup_logger(__name__)

def leaveRecord_menu():
    db = SessionLocal()
    while True:
        print("====Leave Record Management Menu:====")
        print("1. Add New Leave Record")
        print("2. View All Leave Records")
        print("3. View Leave Records by Employee ID")
        print("4. Update Leave Record Status")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                emp_id = int(input("Enter employee ID: "))
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                reason = input("Enter reason for leave: ")
                leave_type = input("Enter leave type (casual/sick/vacation/personal): ").lower()

                leave_data = LeaveRecordCreate(
                    emp_id=emp_id,
                    start_date=start_date,
                    end_date=end_date,
                    reason=reason,
                    leave_type=LeaveTypeEnum(leave_type)
                )

                leave_record = add_leave_record(db, leave_data)
            except Exception as e:
                logger.error(f"Error adding leave record: {e}")
                raise

        elif choice == '2':
            view_all_leave_records(db)

        elif choice == '3':
            try:
                emp_id = int(input("Enter employee ID to view leave records: "))
                view_leave_records_by_employee(db, emp_id)
            except Exception as e:
                logger.error(f"Error viewing leave records by employee: {e}")
                raise

        elif choice == '4':
            leave_id = int(input("Enter leave record ID to update status: "))
            new_status = LeaveStatusEnum(input("Enter new status (pending/approved/rejected): ").lower())
            update_leave_record_status(db, leave_id, new_status)

        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")

            
    db.close()