#Float array in Python
import array 

arrFloat = array.array('f',[1.1,2.2,3.3,1.4,1.5])  #float array

print("Float array is given below: ")
for x in range (len(arrFloat)):
    print("{0:.2f}".format(arrFloat[x]))
