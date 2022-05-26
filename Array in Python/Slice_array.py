#slice array  in Python

import array as arr

numArr =  arr.array('i',[10,20,30,40,50,60,70,80,90,100])

print("All array items are: ",numArr)

#now we will slising our array

print(numArr[3:6])   #4th element to 6th

print(numArr[:-3])  #beginging to 7th

print(numArr[3:])  #4th to end


print(numArr[:])  #beginging to end
