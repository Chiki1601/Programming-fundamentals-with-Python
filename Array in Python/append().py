#append items in existing array

import array as arr

numArr = arr.array('i',[10,20,30,40,50,60,70,80,90,100])
print("Array items are: ")
print(numArr)

#adding item at the end

numArr.append(110)
print("\n array items after Adding an item: ")
print(numArr)


numArr.append(120)
numArr.append(130)
numArr.append(140)
numArr.append(150)
print("\n array items after Adding an item: ")
print(numArr)
