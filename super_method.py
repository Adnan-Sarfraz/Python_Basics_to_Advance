class car:
    def __init__(self, type):
        self.type=type
    @staticmethod
    def stop():
        print("STOPPED")
    @staticmethod
    def start():
        print("START")

class ToyotaCar(car):
    def __init__(self, type, name):
        #way to call the super method
        super().__init__(type)
        self.name=name      

car1= ToyotaCar("prius", "electric")
print(car1.name)
print(car1.type)

        