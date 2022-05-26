#selection sort in Python

def Selection_sort(arr):
    for  i in range(len(arr)):
        min = i
        
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
            arr[min],arr[i] = arr[i],arr[min]
            
        return arr
    
myArr = [11,1,77,84,9]

print("Array before sorting:",myArr)
Selection_sort(myArr)           
        
        
print("\n\n Array after sorting:",myArr) 
