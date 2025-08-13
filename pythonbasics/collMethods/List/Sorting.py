l=[75,34,67,89,12,98,9]
'''i=0
j=i+1
k=0
for i in <=len(l):
    if l[i]>l[j]:
        k=l[i]
        l[i]=l[j]
        l[j]=k
    else:
        j+=1    
    i+=1
print(l) ''' 

for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i]>l[j]:
           l[i],l[j]=l[j],l[i]
        else:
            pass    
print(l)        

k=l.sort(reverse=True)
print(k)