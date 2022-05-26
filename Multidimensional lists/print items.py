#acess via loop in Python

mList = [
    
    [1,2,3,4,5],
    [6,7,8],
    [10,11]
]


for  i in range(len(mList)):
    for j in range(len(mList[i])):
        print(mList[i][j],end="")
    print()
