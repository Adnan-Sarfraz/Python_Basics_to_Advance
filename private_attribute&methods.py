class bank:
    #private attribute created 
    __name = "Anonymous"

    #private method created 

    def __function(self):
        print("hello my name is adnan")
    def welcome(self):
        self.__function() 



 #you cannot directly acces the private method via calling them... you havt to create a 
 #public method and call them 
b = bank()
b.welcome()
