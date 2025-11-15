#ABSTRACTION--> to hide the unnessesory things and show only what is necessesory to the user
class car:
 def __init__(self):
  self.accilerator=False
  self.breeak=False
  self.clutch=False

 def start(self):
  self.clutch=True
  self.accilerator=True 
  self.breeak=False
  print("Car is stared.. ")
  
# just accessesing these things to the user means abstraction 
c1=car()
c1.start()  