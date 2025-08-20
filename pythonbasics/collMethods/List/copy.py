l=[3,4,5,"om","5"]
l2 = l[::]                       
l2[2]="hello"
l3= l2.copy()
print(l)
print(id(l))
print(id(l2))        