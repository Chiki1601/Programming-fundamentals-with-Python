#how can we add the item in dicitonary
#in Python 


bike = {
    
    "brand": "Honda",

"model" : "xyz",
    
    "year" : "2023",
    "engine":"220cc",

}

print("Dicitonary data is given by: ")

for x in bike.items():
    print(x)
    
bike["color"] = "Jet Black"

print("\n\nDicitonary data is given by(After adding the color of bike): ")

for x in bike.items():
    print(x)
