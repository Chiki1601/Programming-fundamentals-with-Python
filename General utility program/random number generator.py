#random number generator

import random
num = int(input("Enter the no of random numbers: "))
max = int(input("Enter the maximum value of random number: "))
print(num,"random numbers between 0 to",max)
for i in range(num):
    print(random.randint(0,max))
