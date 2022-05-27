# swap without third varuable
x =  int(input("Enter N number: "))
y =  int(input("Enter N number: "))

print("Before Swapping \n X = ",x,"Y = ",y)

x = x+y
y = x-y
x = x-y

print("After Swapping \n X = ",x,"Y = ",y)
