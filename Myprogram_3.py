#Royce Daniel, 4/10/2026, "Employees marked for termination"
class Employee:
    def __init__(self,name,ID, department, title):
        self.name = name
        self.ID = ID
        self.department = department
        self.title = title

Employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice president")
Employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
Employee3 = Employee("Joy Jones", 81774, "Manufacturing", "Engineer")
print("Employees marked for termination:")
print("Name:",Employee1.name,"ID:,",Employee1.ID, "Department:", Employee1.department, "Title:", Employee1.title)
print("Name:",Employee2.name,"ID:,",Employee2.ID, "Department:", Employee2.department, "Title:", Employee2.title)
print("Name:",Employee3.name,"ID:,",Employee3.ID, "Department:", Employee3.department, "Title:", Employee3.title)