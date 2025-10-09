"""
class variables :   1. instance var
                    2. ststic var
                    3. local var

method types      :   1. instance method
                      2. class method
                      3. static method


"""
# class myclass():
#     def __init__(self):
#         self.x = 10
#         print("constructor calls itself")
#         self.y = 20
#     def m1(a):
#         print(a.x)
#         print(a.y)      
      

# m = myclass()
# m.m1()



class myclass():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("constructor calls itself")
        
    def m1(a):
        print(a.x)
        print(a.y)      
      

m = myclass(10,20)
m.m1()