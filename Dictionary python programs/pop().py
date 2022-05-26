#   today we will see how can we remove the item using pop() in Python  Dictionary

bike = {
    
    "brand": "Honda",

"model" : "xyz",
    
    "year" : "2023",
    "engine":"220cc",

}

print("Dicitonary data is given by: ")

for x in bike.items():
    print(x)

    
    
bike.pop("engine")
print("\n Data of Bike dictionary after removing engine: ")

for x in bike.items():
    print(x)
