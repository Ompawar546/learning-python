#deleting element isc set


s={3,4,5,6,"hello","om",66}
s1={4,5,6,7,"hello"}
s.remove(4)
s.discard("om")
s.discard(4444)
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.clear()
print(s)