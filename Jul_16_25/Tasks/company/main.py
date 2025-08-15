from employee import Developer, Manager, CTO
from payroll import Payroll

dev = Developer("Ravi", 101, 50000)
mgr = Manager("Priya", 102, 70000)
cto = CTO("Kiran", 103, 100000)
emp_lst=[dev,mgr,cto]

for emp in emp_lst:
    emp.display_info()

payroll = Payroll()
payroll.process_payroll(emp_lst)

Payroll.change_company_name("sculptsoft")
