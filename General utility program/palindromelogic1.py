#palindrome Logic 1

str = input("Enter the string to check palindrome or not: ")

str = str.casefold()

if(str==str[::-1]):
    
    print("Yes, it is palindrome")
    
else:
    print("No, it is not a palindrome")
