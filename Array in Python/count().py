#count() method in Python array


import array as arr

numA = arr.array('i',[10,20,30,10,10,20,20,30,30,10,20,10,20,10,20]) #  n(30)= 3

print("Array is :",numA)

n = numA.count(30)

print("Total count of 30 in the array is: ",n)
