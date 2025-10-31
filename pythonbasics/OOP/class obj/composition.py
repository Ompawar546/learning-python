
#using properties of other classes  (has a relation)
class myclass():
    def __init__(self,name,age):
        self.name  = name
        self.age = age
    def details(self):
        print(self.name)
        print(self.age)    
            
class students():
    def __init__(self,qua,exp):
        self.qua = qua
        self.exp = exp
        self.me = myclass("om",22)
    def info(self):
        self.me.details()
        print(self.exp)
        print(self.qua)    

s = students("btech",3)
s.info()        