#reverse() method in Python array


import array as arr
numArr =  arr.array('i',[10,20,30])
print("Array is :",numArr)

numArrRev = numArr[::-1]
print("Array after reverse: ",numArrRev)
