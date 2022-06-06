#sum of digit
n= int(input("Enter the number:"))
sum = 0
while(n>0):
    x = n%10
    sum = sum + x
    n = n//10
print("Sum of digit is: ",sum)