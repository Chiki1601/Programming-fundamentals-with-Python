# prime number logic 1

count = 0
n = int(input("Enter  the number: "))
for i in range(1,n+1):
    if n%i == 0:
        count +=1
        
if count ==2:
    print(n,"is a Prime number")
    
else:
    print(n,"is not a Prime number")
