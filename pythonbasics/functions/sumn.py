l = [2,3,4,5,6,7]
def sumn(x):
    result = 0
    for i in range(1,x+1):
        result = result+i
    return result
for i in l:
    print(sumn(i))
