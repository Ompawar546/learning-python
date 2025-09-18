#set operation
s = {1,22,55,6,7,8}
a = {22,55,8,9,10,12,"donkey"}
print(dir(s))

print(s.intersection(a))
print(s&a)

print(s.union(a))
print(s|a)

print(s.difference(a))
print(s-a)

print(a.symmetric_difference(s))
print(a^s)

print(s.issubset(a))
print(s.issuperset(a))
print(s.isdisjoint(a))

s.difference_update(a)
print(s)