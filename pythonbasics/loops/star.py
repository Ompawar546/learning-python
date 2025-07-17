'''for x in range(1,5):
    print("*"*x)

for row in range(1,5):
    for col in range(1,row+1):
        print("*",end="")
    print()  '''  

   

row = int(input())

for x in range(1,row+1):
    for y in range(1,row-x+1):
        print("x",end="")       
    for c in range(1,x+1):
        print(" ",end="")
    print()    



row = int(input())
for x in range(1, row + 1):
    print(" " * (row - x) + "x" * x)





















