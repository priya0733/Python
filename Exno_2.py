class SalaryNotInRange(Exception):
    def __init__(self,salary,message="salary is not in (5000,15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

salary = int(input("Enter salary amount: "))
pass 

try:
        if not 5000 < salary < 1500:
             raise SalaryNotInRange(salary)
        print("success")
except:
        print("Invalid")
    
    

    
    