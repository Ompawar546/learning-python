class myclass():
    def __init__(self):
        self.name = "om"
        self.age = 22
    def instmeth():
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


y  = childclass()
# print(y.name)
# print(y.age) gives error coz child class has its own constructor and object 

y.classmeth()
y.instmeth()
y.statmeth()