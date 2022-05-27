#largest among a digit
arr = []

num = int(input("Enter N number: "))
for n in range(num):
    numbers = int(input("Enter number:"))
    arr.append(numbers)
    
print("Maximum element in the list is: ",max(arr))
print("Minimum element in the list is: ",min(arr))
