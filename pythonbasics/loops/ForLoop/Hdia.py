a = 5
for i in range(a):
    for j in range(i+1):
        print(" ",end=" ")
    for p in range(i,a):
        print("*", end=" ")    
    print()


print("----------------------------------------------------------")


for i in range(a):
    for j in range(i,a):
        print(" ", end=" ")
    for p in range(i):
        print("*",end=" ") 
    for q in range(1,i):
        print("*",end=" ")         
    print()
for r in range(a):
    for c in range(r):
        print(" ",end=" ")
    for z in range(r,a):
        print("*", end=" ") 
    for y in range(r+1,a):
        print("*", end=" ")       
    print()         

print("----------------------------------------------------------")

for i in range(a):
    for j in range(i+1):
        print(" ",end=" ")
        if j==i or j==a :
            print("*",end=" ")  
    print()




print("-------------------------------------------")


for i in range(a):
    for j in range(i+1):
        print(j, end=" ")
    print()  
print("----------------------------------------------------------")


for i in range(a):
    for j in range(i+1):
        print(chr(65+j), end=" ")
    print()        


print("----------------------------------------------------------")
for i in range(a):
    for j in range(i+1):
        print(i, end=" ")
    print()      



print("----------------------------------------------------------")
new=0
for i in range(a):
    for j in range(i+1):
        print(new, end=" ")
        new += 1
    print()         


print("----------------------------------------------------------")    
for i in range(a):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(a,i,-1):
        print(k, end=" ")
    print() 

for i in range(a):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(a,i,-1):
        print(k, end=" ")
    print() 
print("----------------------------------------------------------")
for i in range(a):
    for j in range(i,a):
        print(" ",end=" ")
    for k in range(i+1):
        print(k, end=" ")
    print()     
