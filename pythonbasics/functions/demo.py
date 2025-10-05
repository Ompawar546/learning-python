def outerfun():
    print("1")
    print("2")
    def innerfun():
        return "3,4"
    global inner
    inner = innerfun()   
    print("5")
    print("6") 
 
outerfun() 
print(inner)