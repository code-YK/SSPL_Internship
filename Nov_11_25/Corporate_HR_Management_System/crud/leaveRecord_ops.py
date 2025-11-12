from sqlalchemy.orm import Session
from models import LeaveRecord, Employee, Department
from schemas import LeaveRecordCreate
from config.logger_config import setup_logger
import tabulate

logger = setup_logger(__name__)

# add new leave record
def add_leave_record(db: Session, leave_data: LeaveRecordCreate) -> LeaveRecord:

    # Check if employee exists
    employee = db.query(Employee).filter(Employee.emp_id == leave_data.emp_id).first()
    if not employee:
        logger.error(f"Employee with id {leave_data.emp_id} does not exist.")
        raise ValueError(f"Employee with id {leave_data.emp_id} does not exist.")

    new_leave_record = LeaveRecord(
        emp_id=leave_data.emp_id,
        start_date=leave_data.start_date,
        end_date=leave_data.end_date,
        reason=leave_data.reason,
        status=leave_data.status,
        leave_type=leave_data.leave_type,
        approved_by=leave_data.approved_by
    )

    try:
        db.add(new_leave_record)
        db.commit()
        db.refresh(new_leave_record)
        logger.info(f"Added new leave record with id {new_leave_record.leave_id}.")
        return new_leave_record
    except Exception as e:
        logger.error(f"Error adding new leave record: {e}")
        db.rollback()
        raise
    finally:
        db.close()

# view all leave records
def view_all_leave_records(db: Session) -> None:
    leave_records = db.query(LeaveRecord).all()
    if not leave_records:
        logger.info("No leave records found.")
        return []

    record_list = [{
        "leave_id": record.leave_id,
        "emp_id": record.emp_id,
        "start_date": record.start_date,
        "end_date": record.end_date,
        "reason": record.reason,
        "status": record.status.name,
        "leave_type": record.leave_type.name,
        "approved_by": record.approved_by
    } for record in leave_records]

    logger.info("Leave records retrieved successfully.")
    print(tabulate.tabulate(record_list, headers="keys", tablefmt="grid"))
    logger.info(f"Displayed {len(record_list)} leave records.")

def view_leave_records_by_employee(db: Session, emp_id: int) -> None:
    leave_records = db.query(LeaveRecord).filter(LeaveRecord.emp_id == emp_id).all()
    if not leave_records:
        logger.info(f"No leave records found for employee id {emp_id}.")
        return []

    record_list = [{
        "leave_id": record.leave_id,
        "emp_id": record.emp_id,
        "start_date": record.start_date,
        "end_date": record.end_date,
        "reason": record.reason,
        "status": record.status.name,
        "leave_type": record.leave_type.name,
        "approved_by": record.approved_by
    } for record in leave_records]

    logger.info(f"Leave records for employee id {emp_id} retrieved successfully.")
    print(tabulate.tabulate(record_list, headers="keys", tablefmt="grid"))
    logger.info(f"Displayed {len(record_list)} leave records for employee id {emp_id}.")

# update leave record status 
def update_leave_record_status(db: Session, leave_id: int, new_status) -> LeaveRecord:

    # Step 1: Fetch the leave record
    leave_record = db.query(LeaveRecord).filter(LeaveRecord.leave_id == leave_id).first()
    if not leave_record:
        logger.error(f"Leave record with ID {leave_id} not found.")
        return None

    try:
        # Step 2: Fetch the employee and their department
        employee = db.query(Employee).filter(Employee.emp_id == leave_record.emp_id).first()
        if not employee:
            logger.error(f"Employee with ID {leave_record.emp_id} not found for leave {leave_id}.")
            return None

        department = db.query(Department).filter(Department.dept_id == employee.dept_id).first()
        if not department:
            logger.error(f"Department with ID {employee.dept_id} not found for employee {employee.emp_id}.")
            return None

        # Step 3: Update status and approver
        leave_record.status = new_status
        leave_record.approved_by = department.manager_id

        # Step 4: Commit changes
        db.commit()
        db.refresh(leave_record)

        logger.info(
            f"Leave ID {leave_id} updated to status {new_status.name}, "
            f"approved by manager ID {department.manager_id}."
        )
        return leave_record

    except Exception as e:
        db.rollback()
        logger.error(f"Error updating leave record {leave_id}: {e}")
        raise

    finally:
        db.close()