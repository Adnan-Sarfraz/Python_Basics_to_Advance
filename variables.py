#In Python, variables are created when you assign a value to it:

x=1
y="hello world"
print(x)
print(y)

#A variable is created the moment you first assign a value to it.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#so it will print the latest value of x which will be added in the x 

#casting-- specify the data type
a=str("hello adnan")
b=int(10)
c=float(3.0)
print(a)
print(b)
print(c)

#You can get the data type of a variable with the type() function.
d=22
D="adnan dhuddi"
print(d)
print(D) #D will not overirde d

#assigning same value o different variables
e=f=g=0
print(e,f,g)


fruits=["banana", "orange","mango"]
print(fruits)

x = "adnan "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

#global variable
       #variable that declare outside the function is known as global variable 
       #global variable is used inside or outside the function

a="Adnan"

def func():
    b=" is dull"
    print(a+b)
func()


