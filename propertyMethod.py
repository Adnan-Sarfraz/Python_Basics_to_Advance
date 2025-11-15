class Student:
    def __init__(self, chem, phy,math):
        self.chem=chem
        self.phy=phy
        self.math=math


    #if we want to change the value of any subject we can easyily change because if we dont use property
    #method our valuse may be change but the impact of that value might not effect our function
    @property
    def Percentage(self):
     return str((self.phy+self.chem+self.math)/3)+ " %"


s=Student(70,70,70)
print(s.Percentage)
s.math=99
print(s.Percentage)
        