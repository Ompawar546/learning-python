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
    def __init__(self):
        self.qual = "btech"
        self.sal = 90000000
        super().__init__()


y  = childclass()
print(y.name)
print(y.age) 
y.classmeth()
y.instmeth()
y.statmeth()