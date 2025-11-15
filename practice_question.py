class Employee:
    def __init__(self, role, salary, department):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        print(" Salary=> ", self.salary)
        print(" Department=> ", self.department)
        print(" Role=> ", self.role)

#inharitance
class Eng(Employee):
    def __init__(self, name , age ):
     self.name=name
     self.age=age
     super().__init__("Associated Eng", 65000, "IT")

    def ShowDetails(self):
       print(" person name=> ", self.name) 
       print(" person age=> ", self.age)
       return  self.showDetails()

eng=Eng("Adnan Sarfraz", "22")
eng.ShowDetails()

        