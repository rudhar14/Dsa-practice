class employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
    def get_empid(self):
        return self.empid
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    def set_empid(self,empid):
        self.empid=empid
    def set_name(self,name):
        self.name=name
    def set_salary(self,salary):
        self.salary=salary
    
e1=employee(2,"rudhar",59000)

print("Employee ID:", e1.get_empid())
print("Employee Name:", e1.get_name())
print("Employee Salary:", e1.get_salary())
e1.set_salary(60000)
print("Updated Salary:", e1.get_salary())
e1.set_name("Ridhu")        # Update the name
print("updated name:", e1.name)   # Print the updated name
