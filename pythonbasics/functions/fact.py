num  = 5
'''using for loop'''
'''default return type of function is none'''
def factfor(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result

print(factfor(num))    

'''using while loop'''
def fact(x):
    result = 1
    while x>0:
        result = result*x
        x -= 1
    return result

print(fact(num))
