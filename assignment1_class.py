class school:
    def __init__(self, name , PF, OOP, DSA):
        self.name=name
        self.PF=PF
        self.OOP=OOP
        self.DSA=DSA
    def AVG(self):
        sum=self.DSA+self.OOP+self.PF/3
        return sum    
a1=school("ADNAN", 70, 80, 99)
print("AVG-> ",a1.AVG(),"out of 300")
