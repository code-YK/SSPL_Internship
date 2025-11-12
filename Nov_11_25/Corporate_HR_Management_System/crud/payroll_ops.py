from sqlalchemy.orm import Session
from models import Payroll, Employee, LeaveRecord
from schemas import PayrollCreate   
from config.logger_config import setup_logger
import tabulate

logger = setup_logger(__name__)

# view all payroll records
def view_all_payrolls(db: Session) -> None:
    payrolls = db.query(Payroll).all()
    if not payrolls:
        logger.info("No payroll records found.")
        return []

    payroll_list = [{
        "payroll_id": payroll.payroll_id,
        "emp_id": payroll.emp_id,
        "base_salary": payroll.base_salary,
        "allowances": payroll.allowances,
        "deductions": payroll.deductions,
        "net_pay": payroll.net_pay,
        "status": payroll.status.name,
        "pay_date": payroll.pay_date
    } for payroll in payrolls]

    logger.info("Payroll records retrieved successfully.")
    print(tabulate.tabulate(payroll_list, headers="keys", tablefmt="grid"))
    logger.info(f"Displayed {len(payroll_list)} payroll records.")

# get payroll by employee id
def get_payroll_by_emp_id(db: Session, emp_id: int) -> list[Payroll]:
    payrolls = db.query(Payroll).filter(Payroll.emp_id == emp_id).all()
    if not payrolls:
        logger.warning(f"No payroll records found for employee id {emp_id}.")
    
    payroll_list = [{
        "payroll_id": payroll.payroll_id,
        "emp_id": payroll.emp_id,
        "base_salary": payroll.base_salary,
        "allowances": payroll.allowances,
        "deductions": payroll.deductions,
        "net_pay": payroll.net_pay,
        "status": payroll.status.name,
        "pay_date": payroll.pay_date
    } for payroll in payrolls]

    logger.info(f"Payroll records for employee id {emp_id} retrieved successfully.")
    print(tabulate.tabulate(payroll_list, headers="keys", tablefmt="grid"))
    logger.info(f"Displayed {len(payroll_list)} payroll records for employee id {emp_id}.")
    return payrolls

def update_payroll_status(db: Session, payroll_id: int, new_status) -> Payroll:
    payroll = db.query(Payroll).filter(Payroll.payroll_id == payroll_id).first()
    if not payroll:
        logger.error(f"Payroll record with id {payroll_id} not found.")
        return None
    try: 
        payroll.status = new_status

        db.commit()
        db.refresh(payroll)
        logger.info(f"Updated payroll status for id {payroll_id} to {new_status.name}.")
        return payroll
    except Exception as e:
        logger.error(f"Error updating payroll status for id {payroll_id}: {e}")
        db.rollback()
        raise
    finally:
        db.close()
    

# Generate a new payroll for an employee
def generate_payroll_for_employee(db: Session, emp_id: int, pay_date) -> Payroll:
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        logger.error(f"Employee with id {emp_id} does not exist.")
        raise ValueError(f"Employee with id {emp_id} does not exist.")

    leave_deductions = 0.0  # Placeholder for leave deductions logic
    leave = db.query(LeaveRecord).filter(LeaveRecord.emp_id == emp_id, LeaveRecord.status == 'approved').all()
    for record in leave:
        leave_days = (record.end_date - record.start_date).days + 1
        daily_salary = employee.salary / 30  # Assuming 30 days in a month
        leave_deductions += daily_salary * leave_days
    
    base_salary = employee.salary
    allowances = base_salary * 0.2  # 20% allowances
    deductions = leave_deductions
    net_pay = base_salary + allowances - deductions

    new_payroll = Payroll(
        emp_id=emp_id,
        base_salary=base_salary,
        allowances=allowances,
        deductions=deductions,
        net_pay=net_pay,
        status='pending',
        pay_date=pay_date
    )
    try:
        db.add(new_payroll)
        db.commit()
        db.refresh(new_payroll)
        logger.info(f"Generated new payroll record with id {new_payroll.payroll_id} for employee id {emp_id}.")
        return new_payroll
    except Exception as e:
        logger.error(f"Error generating payroll record for employee id {emp_id}: {e}")
        db.rollback()
        raise
    finally:
        db.close()

