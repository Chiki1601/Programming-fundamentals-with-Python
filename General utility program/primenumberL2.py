# prime number logic 2

x  = 2 

ch = 0
n = int(input("Enter  the number: "))

if n<=1:    
    ch = 1
    
while x<=n/2:
    if n%x ==0:
        ch = 1
        break
        
    else:
        x+=1
        
if ch == 0:
    print(n,"is a Prime number")
    
else:
    print(n,"is not a Prime number")
