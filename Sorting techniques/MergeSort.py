#merge sort in Python

def merge_sort(myList):
    if len(myList) > 1:
        mid = len(myList)//2
        left = myList[:mid]
        right = myList[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = 0
        j = 0
        k  =0
        
        while i < len(left) and j< len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i += 1
                
            else:
                myList[k] = right[j]
                j += 1
            k += 1
            
            
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k +=1
            
            
        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
            
        
         
        
        
            
myArray = [23,11,85,7,47,28,55]
            
print("Array before sorting: ",myArray)
merge_sort(myArray)
        
print("\n\nArray after sorting: ",myArray)   
          
