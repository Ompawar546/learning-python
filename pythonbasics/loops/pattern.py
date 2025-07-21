row = 6
for i in range(1,row+1):
    for j in range(1,row+1):
        if j == 1 or j == i or i == row:
            print("*", end="")
        else:
            print(" ", end="")    
    print()       


print("                                     ")



for i in range(1,6):
    for j in range(1,row+1):
        if j==5 or i==5 or i+j==6:
            print("*",end="")
        else:
            print(" ",end="")
    print()        

print("                                     ")

for i in range(1,6):
    for j in range(1,6):
        if i==1 or j == 5 or i==j:
            print("*", end="")
        else:
            print(" ", end="")
    print()            



for i in range(1,6):
    for j in range(1,6):
        if i==1 or j == 1 or i+j==6 :
            print("*", end="")
        else:
            print(" ", end="")
    print()      