class Car:
    colour = "black"
    @staticmethod
    def start():
        print("car is started...")
    @staticmethod #static method is used at the class level
    def stop():
        print("car stopped....")


#syntax of inheritence 
class ToyotaCar(Car):
    def __init__(self, name ):
        self.name=name

    def CarName(self):
        print("you aare the owner of this car ", self.name)

c=ToyotaCar("fortuner")

c.CarName()
print(c.colour)
c.start()
c.stop()



c=ToyotaCar("prius")
c.CarName()
print(c.colour)
c.start()
c.stop()
