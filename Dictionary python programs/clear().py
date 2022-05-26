#how can we remove all items using clear() method in Python  Dictionary


bike = {
    
    "brand": "Honda",

"model" : "xyz",
    
    "year" : "2023",
    "engine":"220cc",

}

print("Dicitonary data is given by: ")

for x in bike.items():
    print(x)
    
bike.clear()
print("\n Data of Bike dictionary after removing all items: ",bike)

