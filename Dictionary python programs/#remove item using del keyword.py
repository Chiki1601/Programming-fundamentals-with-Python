#remove item using del keyword

bike = {
    
    "brand": "Honda",

"model" : "xyz",
    
    "year" : "2023",
    "engine":"220cc",

}

print("Dicitonary data is given by: ")

for x in bike.items():
    print(x)
    
del bike["engine"]

print("\n Data of Bike dictionary after removing engine: ")

for x in bike.items():
    print(x)
