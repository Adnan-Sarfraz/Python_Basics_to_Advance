class complex:
    def __init__(self, real, imaginary):
        self.imaginary=imaginary
        self.real=real

    def shownumber(self):
        print(self.real," i+1", self.imaginary," j")

    def __add__(self,num2):
        newReal=self.real+num2.real
        newImaginary=self.imaginary+num2.imaginary
        return complex(newReal,newImaginary)
    

    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImaginary=self.imaginary-num2.imaginary
        return complex(newReal,newImaginary)
    

    def __mul__(self,num2):
        newReal=self.real+num2.real
        newImaginary=self.imaginary+num2.imaginary
        return complex(newReal,newImaginary)
    

 


num1=complex(3,1)               
num1.shownumber()

num2=complex(5,3)
num2.shownumber()

num3=num1+num2
num3.shownumber()

num3=num1-num2
num3.shownumber()

num3=num1*num2
num3.shownumber()



        