def recfun(n):
    if n==1 or n==0:
        return 1
    else:
        return n*recfun(n-1)

print(recfun(5))


def addno(n):
    if n == 0:
        return 0
    return n+addno(n-1)

print(addno(5))