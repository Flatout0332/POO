class Main:
    def __init__(self):
        self.employee_hours = 48
        self.employee_salary_hour = 5000
        self.employee_retention = 0.125
    
    
    
    def calculate(self):
        self.employee_salary = self.employee_hours * self.employee_salary_hour
        self.employee_retention_amount = self.employee_salary * self.employee_retention
        self.employee_net_salary = self.employee_salary - self.employee_retention_amount
        
    def display(self):
        self.calculate()
        print(f"Salario del empleado: {self.employee_salary}")
        print(f"Cantidad de retención: {self.employee_retention_amount}")
        print(f"Salario neto del empleado: {self.employee_net_salary}")

main = Main()
main.display()
