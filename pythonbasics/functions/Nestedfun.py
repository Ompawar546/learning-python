def outerfun():
    print("1")
    print("2")
    def innerfun():
        print("3,4")     
    print("5")
    print("6") 
    return innerfun 


inner = outerfun()
print(inner())