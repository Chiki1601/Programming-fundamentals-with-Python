#palindrome number

n = int(input("Enter the number: "))

temp = n
rev = 0
while(n>0):
    d = n%10
    rev = rev*10 + d
    n = n//10
    
if(temp == rev):
     print("Yes, it is palindrome")
    
else:
    print("No, it is not a palindrome")
    
    
