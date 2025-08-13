l=[23,45,67,78,98,3]
n=int(input())
i=0
for j in l:
    if j==n:
        print(i)
        break
    else:
        i+=1

print(l.index(n))
