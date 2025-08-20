l=[3,4,"om",6,7,77]
l2=l                        # does not create seprate object fot l2
l2[2]="hello"

print(l)
print(id(l))
print(id(l2))        