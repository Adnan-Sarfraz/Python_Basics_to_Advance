try:
    l=[1,2,3,4]
    i=int(input("Enter the number "))
    print(l[i])
except:
    print("Some error accured ")
    
#finally will always executed at every cost 
finally:
    print("Finally will always is executed  ")