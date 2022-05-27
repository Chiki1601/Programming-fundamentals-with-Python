#palindrome Logic 2

s1 = input("Enter the string to check palindrome or not: ")
s2 = ""

for i in s1:
    s2 = i+s2
    
if(s1==s2):
    print("Yes, it is palindrome")
    
else:
    print("No, it is not a palindrome")
    
        
