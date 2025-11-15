'''a=10
b=20
if a>b:
    print("A is greater then B")
elif a==b:
    print("A is equal to B")
else:
    print("A is not greator then B")        '''

n = int(input("Enter The Value of N: "))

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and n >= 2 and n <= 5:
    print("Not Weird")
elif n % 2 == 0 and n >= 6 and n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
