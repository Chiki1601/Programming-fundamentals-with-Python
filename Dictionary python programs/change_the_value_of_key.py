#change the value of a key

#itemes() method in python dictionary

bike = {
    
    "brand": "Honda",

"model" : "xyz",
    
    "year" : "2023",
    "engine":"220cc",

}

print("Dicitonary data is given by: ")

for x in bike.items():
    print(x)
    
    
bike["brand"] = "Bajaj"

print("\n\nDicitonary data is given by(After modification): ")

for x in bike.items():
    print(x)
    
        
bike["model"] = "pqr"

print("\n\nDicitonary data is given by(After modification): ")

for x in bike.items():
    print(x)
