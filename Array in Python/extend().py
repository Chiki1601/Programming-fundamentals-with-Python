#how to add two arrays usiong Extend() method

import array as arr

numA = arr.array('i',[10,20,30])
numB = arr.array('i',[100,200,300])


print("Array A is: ",numA)
print("Array B is: ",numB)


numA.extend(numB)
print("Array A after extend(): \n ",numA)
