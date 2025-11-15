#class creation
class student:
    name="Adnan Sarfraz"
#making object to access class
s1=student()     
print(s1.name)

#constructor / __init__ functiion
class students:
    def __init__(self, fullname):
        self.name=fullname

s2=students("Ali")
print(s2.name)
s3=students("Adhmed")
print(s3.name)  

#-----------EX2---------------
class students2:
    def __init__(self, name , marks ):
        self.name=name
        self.marks=marks 

s1=students2("adnan sarfraz", 90)
s2=students2("faizan akram", 88)
s3=students2("muawiah", 94)
print(s1.name , s1.marks)   
print(s2.name , s2.marks) 
print(s3.name , s3.marks)      

#-------------------METHODS-------------------#
class ABC:
    def __init__(self, name, marks, gpa, reg_no):
        self.name=name
        self.marks=marks
        self.gpa=gpa
        self.reg_no=reg_no

    def welcome(self):
        print("Welcome student")

    def Get_Name(self):
        return self.name
     
    def Get_Marks(self):
        return self.marks
    
    def Get_GPA(self):
        return self.gpa
    
    def Get_RegNo(self):
        return self.reg_no

a1=ABC("Adnan Sarfraz", 88, 2.7, 47)
a1.welcome()
print("Name-> ",a1.Get_Name())
print("Marks-> ",a1.Get_Marks())
print("GPA-> ",a1.Get_GPA())
print("RegN0-> ",a1.Get_RegNo())
