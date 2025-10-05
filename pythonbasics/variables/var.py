x =  50         #global variables 
y = 60


def myfun():
    global a 
    global b
    a,b = 99,89


def myfun2():
    x,y=100,200
    print(x,y)
    print(globals()['x'],globals()['y'])
    print(a,b)


myfun2()

    