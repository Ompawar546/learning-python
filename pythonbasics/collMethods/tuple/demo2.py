t = 3,1,7,4,9,3,5
k=list(t)
for i in range(0,len(k)):
    for j in range(0,len(k)):
        if k[i]>k[j]:
            k[i],k[j]=k[j],k[i]
        else:
            pass

z=tuple(k)
print(z)
print(t.__contains__(9))

