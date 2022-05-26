#insertion sort in Python


def Insertion_sort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        pos = i
        
        while pos > 0 and arr[pos-1]>temp:
            arr[pos] = arr[pos-1]
            pos = pos-1
        arr[pos] = temp
        
    return arr


my_arr = [74,11,7,14,35]

print("Array before Sorting:",my_arr)

Insertion_sort(my_arr)

print("\n\nArray after Sorting:",my_arr)
