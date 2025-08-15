class Payroll:
    company_name='Techcorp'
    
    @classmethod
    def change_company_name(cls,new_company_name):
        cls.company_name=new_company_name
        print('Changing company name to sculptsoft')
    
    @staticmethod
    def greet():
        print('Processing Payroll for TechCorp')
    
    def process_payroll(self,emp_lst):
        Payroll.greet()
        for emp in emp_lst:
            print(f'''{emp.name}'s salary : {emp.calculate_salary()}/-''')

    