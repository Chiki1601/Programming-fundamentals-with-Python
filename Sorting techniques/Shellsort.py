#shell sort
def shell_sort(array,n):
    gap = n//2
    while gap>0:
        for i in range(gap,n):
            temp = array[i]
            j = i
            while j>= gap and array[j-gap]>temp:
                array[j] = array[j - gap]
                j-= gap
            array[j] = temp
        gap //=2
        
myArr = [11,33,22,44,66]
size = len(myArr)

print("Array before sorting: ",myArr)
shell_sort(myArr,size)

print("\n\nArray after sorting: ",myArr)
