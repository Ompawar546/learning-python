print("----------------------------------------------------------")

a=5

for i in range(a):
    for j in range(i,a):
        print(" ",end=" ")
    for k in range(i+1):
        print(i, end=" ")
    for l in range(1,i+1):
        print(i, end=" ")
    print() 


