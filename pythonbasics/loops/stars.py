row = 6
for x in range(1,row+1):
    for y in range(1,x):
        print("*",end="")
    print()    


for x in range(2,row+1):
    for y in range(row,x,-1):
        print("*",end="")
    print()        