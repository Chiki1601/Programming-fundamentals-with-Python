#Heap sort program in Python

def heapify(arr,n,i):
    maxi = i
    left  = 2*i + 1
    right = 2*i + 2
    
    if left <n and arr[i]< arr[left]:
        maxi = left
        
    if right < n and arr[maxi] < arr[right]:
        maxi = right
        
    if maxi!= i:
        arr[i], arr[maxi] =  arr[maxi], arr[i]
        heapify(arr,n,maxi)
        
def heapSort(arr):
    n = len(arr)
    
    for i in range(n,-1,-1):
        heapify(arr,n,i)
        
    for i in range(n-1,0,-1):
        arr[i], arr[0] =  arr[0], arr[i]  #swap
        
        heapify(arr,i,0)
        
myArr = [93,11,8,67,33,12]


print("Array before sorting:",myArr)

heapSort(myArr)
        
        
print("\n\n Array after sorting:",myArr) 
