from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,emp_id,salary):
        self.name=name
        self._emp_id=emp_id
        self.__base_salary=salary        
    
    @abstractmethod
    def calculate_salary(self):
        pass

    def display_info(self):
        print(f'''Name : {self.name}
Employee_Id : {self._emp_id}
Base Salary : {self.__base_salary}/-''')
        print('--'*12)
        
    def get_base_salary(self):
        return self.__base_salary

class Manager(Employee):
    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id, salary)

    def calculate_salary(self):
        return (super().get_base_salary() + 10000)

class Developer(Employee):
    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id, salary)

    def calculate_salary(self):
        return (super().get_base_salary() + 5000) 

class CTO(Manager,Developer):
    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id, salary)

    def calculate_salary(self):
        return (super().get_base_salary() + 20000) 
