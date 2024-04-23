#defining the class
class Employee: #super class
    def __init__(self, employee_name, employee_number): #initializing instances of the class with the listed attributes
        self.employee_name=employee_name #employee name
        self.employee_number=employee_number #employee number

    #getter methods for Employee class
    def get_employee_name(self):
        return self.employee_name
    
    def get_employee_number(self):
        return self.employee_number
    
    #setters for Employee class
    def set_employee_name(self, employee_name):
        self.employee_name=employee_name

    def set_employee_number(self, employee_number):
        self.employee_number=employee_number

    def __str__(self):
        return f"\nEmployee Information:\n\nName: {self.employee_name}\nEmployee Number: {self.employee_number}\n"
    
#subclass of Employee
class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay): #adds two additional 
        super().__init__(employee_name, employee_number)
        self.shift_number=shift_number
        self.hourly_pay=hourly_pay
        self.shift=self.set_shift_number(shift_number)

    #getters for ProductionWorker class
    def get_shift_number(self):
        return self.shift_number
    
    def get_hourly_pay(self):
        return self.hourly_pay
    
    #setters for ProductionWorker class
    def set_shift_number(self, shift_number):
        self.shift_number=shift_number
        if shift_number==1:
            return "Day Shift"
        elif shift_number==2:
            return "Night Shift"
        else:
            return "Please enter either 1 or 2 for shift number."

    def set_hourly_pay(self, hourly_pay):
        self.hourly_pay=hourly_pay

    def __str__(self):
        return super().__str__()+"Shift: "+self.shift+"\nHourly wage: "+str(self.hourly_pay)+"\n"
    
def main():
    name=input("Please enter employee's full name: ")
    number=int(input("Please enter employee number: "))
    shift=int(input("Please enter shift number: "))
    pay=float(input("Please enter hourly wage: "))
    
    employee1=ProductionWorker(name, number, shift, pay)

    print(employee1)
    

main()