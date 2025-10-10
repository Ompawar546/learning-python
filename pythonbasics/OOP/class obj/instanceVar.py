class myclass():
    def __init__(self):
        self.x = 10
        self.y = 20
    def m1(self):
        print(self.x)
        print(self.y)

a = myclass()
b = myclass()
b.m1()
b.x = 0
b.m1()


