"""
instance var : value changes object to object

"""


"""here no instacne variable are created even if we create an object of myclass hence error """
class myclass():
    def __init__(self):
        print("no instance var")
    def m1(self,name,course):
        self.name = name
        self.course = course
    def m2(self):
        print(self.name)
        print(self.course)        

x = myclass()
"""for creating instance var call that instance method"""
x.m1("soham","ml")
x.m2()

y= myclass()
y.m1("adil","java")
y.m2()
print(y.__dict__)
print(myclass.__dict__)
y.time = "11 Am"       """creating an instance var outside the class"""
print(y.__dict__)


