class myclass():
    def __init__(self):
        self.name = "om"
        self.age = 22
    def instmeth(self):
        print("instanace method")
    @classmethod
    def classmeth(cls):
        print("class method")
    @staticmethod
    def statmeth():
        print("stat method")    

class childclass(myclass):
    pass


y  = childclass()
print(y.name)
print(y.age)

y.classmeth()
y.instmeth()
y.statmeth()