#nuumber of objecsts created for a class
class myclass:
    count = 0
    def __init__(self):
        myclass.count = myclass.count+1

obj1 = myclass()
obj2 = myclass()
obj3 = myclass()
print(myclass.count)        