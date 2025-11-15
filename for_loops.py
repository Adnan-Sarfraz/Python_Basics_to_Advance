#for loop with strings
#1-->
name='adnan'
for i in name:
    print(i)
print('' \
'' \
'' \
'')
#2-->
name='aslam'
for i in name:
    print(i)
    if(i=='a'):
        print("adnan sarfraz")
print('' \
'' \
'' \
'')        
#3-->          
#for loop with list
x=['apple','banana','orange']
for a in x:
    print(a)             
print('' \
'' \
'' \
'')
#4-->
#example with dictionary(DICT)
x={'Name':'Adnan Dhuddi',
    'Age':22,
     'Learning':'For-loops in pyhon',
      'Degree':'Computer science',
       'Email':'dani.sarfraz@gmail.com',
        'Area Postal-Code':749,
        'Phone Number':923108664544
         }
for key, value in x.items():#key means -->name, age, phone number etc<--
    print(key, ':', value )  #value means the value corresponding to the keys
print('' \
'' \
'' \
'')
#5-->
#loops with touples 
touple=('apple','banana','orange')
for b in touple:
    print(b)  
print('' \
'' \
'' \
'')
#6-->
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":#if it finds banana it will stop
    break
   
print('' \
'' \
'' \
'')
 #                            <--RANGE FUNCTION-->
 #1--> 
for x in range(10):#it will print till N-1
   print(x) 

print('' \
'' \
'' \
'')
#2-->
#first peremeter is starting index and second one is ending index
for x in range(10, 20):
   print(x)

print('' \
'' \
'' \
'')
#3-->
#first peremeter is starting index and second one is ending index and third one is step/jump
for x in range (1,20,2):
   print(x)

print('' \
'' \
'' \
'')
#4-->
for x in range(6):
  if x == 7:
     break
  print(x)
else:
  print("Finally finished!")

print('' \
'' \
'' \
'')

#                           -->NESTED LOOPS<--

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)