#convert hexadecimal to octal
print("Enter 'x' for exit")

hexadec = input("Enter a number in Heexadecimal Format: ")

if hexadec == 'x':
    exit()
    
else:
    dec = int(hexadec,16)
    print(hexadec,"in Octal = ",oct(dec))
