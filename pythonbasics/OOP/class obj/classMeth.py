class myclass():
    @classmethod 
    def clsMeth(cls):
        print("class method")


obj = myclass()
obj.clsMeth()
print(type(obj.clsMeth))