l=[11,23,34,45,11,32,11,45,11]
n=int(input())
j=0
count = 0
for i in l:
    if i==n:
        print(j)
        count+=1
    else:
        j+=1    
print(count)        
