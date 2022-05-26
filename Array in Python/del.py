#how can we remove items using del keyword

import array as arr

numArr =  arr.array('i',[10,20,30,40,50,60,70,80,90,100])
print("All array items are: ",numArr)


#removing an item at 3rd index

del numArr[3]


print("All array items are (After removing 3rd index): ",numArr)


# now we will deleting whole array


del numArr

print("\n numArr is deleted")
