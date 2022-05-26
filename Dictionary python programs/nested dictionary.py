#nested dictionary

laptop = {  "brand": "MacBook","os ": "Mac OS" }

mobile = {  "brand": "iPhone","os ": "iOS"  }



Apple = {
    "laptop ":laptop,  "mobile": mobile  
}

print("Apple products:")

for x in Apple.items():
    print(x)
