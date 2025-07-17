s = [3,78,65,255,56]  
print(type(s))
b = bytes(s)
print(b)

print(b[2])

for x in b:
    print(x)


print("------------------------------------------")
x = range(2,10)
for value in x :
    print(value)


print("------------------------------------------")
z= range(100,200, 10 )
for x in z:
    print(x)
