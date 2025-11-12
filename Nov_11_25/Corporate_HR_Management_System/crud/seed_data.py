from config.db import SessionLocal, Base, engine
from models import *
from config.enum import GenderEnum, LeaveStatusEnum, LeaveTypeEnum, PayrollStatusEnum
from datetime import date
from config.logger_config import setup_logger

logger = setup_logger(__name__)
def seed_data(db):

    logger.info("Seeding data...")
    # Seed Departments
    departments = [
        Department(name="Human Resources", manager_id=1, budget=750000),
        Department(name="Finance", manager_id=2, budget=950000),
        Department(name="Engineering", manager_id=3, budget=1500000),
        Department(name="Marketing", manager_id=4, budget=800000),
    ]
    db.add_all(departments)
    db.commit()

    # Seed Employees
    employees = [
        Employee(name="Raj Patel", email="raj.patel@corp.in", gender=GenderEnum.male,
                 hire_date=date(2021, 6, 10), dept_id=1, salary=65000),
        Employee(name="Priya Mehta", email="priya.mehta@corp.in", gender=GenderEnum.female,
                 hire_date=date(2020, 3, 15), dept_id=2, salary=90000),
        Employee(name="Aman Sharma", email="aman.sharma@corp.in", gender=GenderEnum.male,
                 hire_date=date(2019, 9, 25), dept_id=3, salary=120000),
        Employee(name="Sneha Reddy", email="sneha.reddy@corp.in", gender=GenderEnum.female,
                 hire_date=date(2022, 2, 5), dept_id=4, salary=70000),
        Employee(name="Karan Singh", email="karan.singh@corp.in", gender=GenderEnum.male,
                 hire_date=date(2023, 7, 12), dept_id=3, salary=85000),
        Employee(name="Neha Verma", email="neha.verma@corp.in", gender=GenderEnum.female,
                 hire_date=date(2021, 11, 18), dept_id=2, salary=78000),
    ]
    db.add_all(employees)
    db.commit()

    # Payrolls
    payrolls = [
        Payroll(emp_id=1, base_salary=65000, allowances=5000, deductions=1000,
                net_pay=69000, status=PayrollStatusEnum.paid, pay_date=date(2025, 10, 31)),
        Payroll(emp_id=2, base_salary=90000, allowances=8000, deductions=3000,
                net_pay=95000, status=PayrollStatusEnum.paid, pay_date=date(2025, 10, 31)),
        Payroll(emp_id=3, base_salary=120000, allowances=10000, deductions=4000,
                net_pay=126000, status=PayrollStatusEnum.paid, pay_date=date(2025, 10, 31)),
        Payroll(emp_id=4, base_salary=70000, allowances=4000, deductions=2000,
                net_pay=72000, status=PayrollStatusEnum.paid, pay_date=date(2025, 10, 31)),
        Payroll(emp_id=5, base_salary=85000, allowances=6000, deductions=3000,
                net_pay=88000, status=PayrollStatusEnum.pending, pay_date=date(2025, 11, 10)),
    ]
    db.add_all(payrolls)
    db.commit()

    # Leave Records
    leaves = [
        LeaveRecord(emp_id=1, start_date=date(2025, 9, 1), end_date=date(2025, 9, 3),
                    reason="Family Function", status=LeaveStatusEnum.approved,
                    leave_type=LeaveTypeEnum.casual, approved_by=2),
        LeaveRecord(emp_id=4, start_date=date(2025, 10, 10), end_date=date(2025, 10, 12),
                    reason="Health Checkup", status=LeaveStatusEnum.approved,
                    leave_type=LeaveTypeEnum.sick, approved_by=1),
        LeaveRecord(emp_id=5, start_date=date(2025, 11, 1), end_date=date(2025, 11, 5),
                    reason="Vacation", status=LeaveStatusEnum.pending,
                    leave_type=LeaveTypeEnum.annual, approved_by=3),
    ]
    db.add_all(leaves)
    db.commit()

    logger.info("Seed data inserted successfully.")

def init_db():
    logger.info("Initializing database...")
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_data(db)
    finally:
        db.close()


if __name__ == "__main__":
    logger.info("Initializing database and inserting seed data...")
    init_db()