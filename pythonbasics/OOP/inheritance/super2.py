class myclass():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def instmeth(self):
        print("instanace method")
    @classmethod
    def classmeth(cls):
        print("class method")
    @staticmethod
    def statmeth():
        print("stat method")    

class childclass(myclass):
    def __init__(self,name,age):
        self.qual = "btech"
        self.sal = 90000000
        super().__init__(name,age)


y  = childclass("om",22)
print(y.name)
print(y.age) 
y.classmeth()
y.instmeth()
y.statmeth()