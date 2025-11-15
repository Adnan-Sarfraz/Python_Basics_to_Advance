x=int(input("Enter your number with in a range of 1, 2, 3: "))
match x: 
    case 1 if x==1:
          print("X is 1 ")
    case 2 if x==2:
        print("X is 2  ") 
    case 3 if x==3:
         print("X is 3 ")
    case _ :
          print("X is any number expect 1, 2, 3 ")