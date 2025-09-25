def myfun(x,y):
    sum = x+y
    mul = x*y
    div = x/y
    return sum,mul,div

def myfun2(x,y):
    def newfun():
        sum = x+y           
        mul = x*y
        div = x/y
        print(sum,mul,div)
    return newfun()

print(myfun(3,4))
print(myfun2(3,4))