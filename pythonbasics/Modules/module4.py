def fun1():
    print("public")

print(__name__)
if __name__ == "__main__":    #when module is called from other module name cahnges to file name or it will be __main__ so if __main__ only then the code can be executed which makes it private 
    def fun2():
        print("private")
    fun2()

       