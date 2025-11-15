class student:
    def __init__(self, name):
        self.name=name
    
s1=student("adnan")
print(s1.name)


# this is how you delete the object student 
del s1

#now we are trying to print the  deleted the the object s1
print(s1.name)