#pascals triangle

def fact(n):
    f = 1
    i = 1
    while i<=n:
        f = f*i
        i +=1
    return f

Lines = int(input("Enter the no.of lines: "))

for x in range(Lines):
    for y in range(x+1):
        print(fact(x)//(fact(y)*fact(x-y))," ",end="")
    print()
    
