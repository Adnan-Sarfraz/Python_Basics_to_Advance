class Car:
    @staticmethod
    def start():
        print("CAR IS STARTED")
    @staticmethod
    def stop():
        print("CAR IS STOPED ")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name=name 


        
class Brand(ToyotaCar):
    def __init__(self, type):
        self.type=type

c1=Brand("diesel")
c2=ToyotaCar("fortuner")                
c1.start()
print(c2.name)


        