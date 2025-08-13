"""program to find uique multiples of element in list"""
l=[25,18,72,49,56]
k=[]
d=[]
for i in l:
    for j in range(1,i):              
        if i%j==0:
            if j in k:
                pass
            else:
                k.append(j)
print(k)

