#"Check if the key exist or not
#in Python  Dictionary


bike = {
    
    "brand": "Honda",

"model" : "xyz",
    
    "year" : "2023",
    "engine":"220cc",

}

print("Dicitonary data is given by: ")

for x in bike.items():
    print(x)
    
    
search = input("Enter the key to be searched: ")

if search in bike:
    print("Yes!",search,"is in the Bike dictionary")
    
else:
    print("NO!!",search,"is in the Bike dictionary")
