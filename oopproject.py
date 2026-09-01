class Employee:
    employee_count=0
    """employee name as private attribute"""
    def __init__(self,employee_id,name,salary):
        self.employee_id=employee_id
        self.__name=name
        self.salary=salary
        Employee.employee_count += 1  
    def display(self):
        print(f'Employee ID is {self.employee_id}')
        print(f'Employee name is {self.__name}')
        print(f'Employee salary is {self.salary}')
    def details(self):
        print(f'Employee ID is {self.employee_id}')
        print(f'Employee name is {self.__name}')
        print(f'Employee salary is {self.salary}')
class Manager(Employee):
    def __init__(self,employee_id,name,salary,team_size):
        self.team_size=team_size
        super().__init__(employee_id,name,salary)
    def details(self):
        super().details()
        print(f'The team size is {self.team_size}')
class Developer(Employee):
    def __init__(self,employee_id,name,salary,programming):
        self.programming=programming
        super().__init__(employee_id,name,salary )
    def details(self):
        super().details()
        print(f'Developer programming is {self.programming}')

        
        
        
emp1=Employee(101,'Lakshmi',25000)
print(emp1.employee_id)
print(emp1._Employee__name)
print(emp1.salary)
emp1.display()
emp1.details()
emp2=Manager(102,'prasanna',25000,5)
emp2.details()
emp3=Developer(103,'manimala',25000,"python")
emp3.details()
print(f"Total employees are {Employee.employee_count}")
#print(dir(emp1))
    
