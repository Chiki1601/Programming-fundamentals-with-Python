# HCF (GCD)

def hcf(a,b):
    while(a!=b):
        if(a>b):
            a = a-b
        else:
            b = b-a
            
    return a

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
print(hcf(a,b))
