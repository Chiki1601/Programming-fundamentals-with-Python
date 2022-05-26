#how can we remove all items using del keyword


bike = {
    
    "brand": "Honda",

"model" : "xyz",
    
    "year" : "2023",
    "engine":"220cc",

}

print("Dicitonary data is given by: ")
for x in bike.items():
    print(x)
    
del bike

print("\n\nDictionary is deleted")
