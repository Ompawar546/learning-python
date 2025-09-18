l="A2B4V7"
l1=[]
l2=[]
for i in l:
    if ("a"<= i <="z" or "A"<= i <="Z"):
        l1.append(i)
    else:
        l2.append(i)    

l1.extend(l2)
for j in l1:
    print(j, end="")