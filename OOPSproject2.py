#Design a console based on "Employee Payroll System" using OOPS concepts in Python.
#the system should calculate the salary for different types of employees using all oops concepts
#Employee - Abstarct Class 
#Full time Employee - child class
#Part time Employee - child class
#salary - encapsulated data
#payroll system - controller(HAS-A)
#output
#Employee Created Successfully
#salary:50000
#employee Created Successfully
#salary:20000
class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
    def CalculateSalary(self):
        pass
class FullTimeEmpolyee(Employee):
    def __init__(self,name,emp_id,Salary):
        super().__init__(name,emp_id)  
        self._Salary=Salary
    def CalculateSalary(self):
        return self._Salary
class PartTimeEmployee(Employee):
    def __init__(self,name,emp_id,hourly_rate,hours_worked):
        super().__init__(name,emp_id)
        self._hourly_rate=hourly_rate
        self._hours_worked=hours_worked
    def CalculateSalary(self):
        return self._hourly_rate * self._hours_worked
class PayrollSystem:
    def __init__(self):
        self.employees=None
    def add_employee(self,emp_type):
        if emp_type=="fulltime":
            self.employees=FullTimeEmpolyee("Alice","FT123",50000)
        else:
            self.employees=PartTimeEmployee("Bob","PT456",100,200)
        return "Employee Created Successfully"
    def get_salary(self):
        return self.employees.CalculateSalary()
payroll=PayrollSystem()
print(payroll.add_employee("fulltime"))
print("Salary:",payroll.get_salary())
print(payroll.add_employee("parttime"))
print("Salary:",payroll.get_salary())
