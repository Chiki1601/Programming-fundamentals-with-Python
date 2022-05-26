#insert() method in python array

import array 

numArr = array.array('i',[10,20,30,40,50])
print("array items are:")
print(numArr)

#inserting the value at index 2

numArr.insert(3,35)
print("\n array items after Adding an item: ")
print(numArr)
