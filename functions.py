#creation of function
def my_function():
    print("Hello, world")
#if you want to run your function-> you have to call it also    
my_function() 


print("                                                             " \
"" \
"" \
"" \
"")


#function with one peremeter 
def my_function2(a):
    print("hello "+ a )
#calling a function with peremeter(a) 
my_function2("adnan")
my_function2("ali")
my_function2("john")    
my_function2("haroon")

print("                                                             " \
"" \
"" \
"" \
"")

#function with 2 peremeters
def my_function3(fname,lastname,age):
    print(fname , lastname , age)
#calling the function with 3 peremeters-> fname,lastname,age 
my_function3("Adnan ", "Sarfraz", 22)
my_function3("Haroon ", "Rasheed", 23)
my_function3("Abdullah ","Ghamis",20) 
my_function3("Muawiah ","Qaiser", 24 )  

print("                                                             " \
"" \
"" \
"" \
"")
#If the number of arguments is unknown, add a * before the parameter name:
def my_function4(*kids):
  print("The youngest child is " + kids[3])

my_function4("Muhammad", "Ali", "Shah" ,"22 years old")