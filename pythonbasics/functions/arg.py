# '''
#  types of arguments 
# 1. positional arguments 
# 2. keyword arguments
# 3. default arguments
# 4. variable length arguments 
# '''

# '''positional args'''
# def myfun(x,y):
#     print(f'first = {x}')
#     print(f'secord = {y}')

# myfun(55,[1,23,4])    

# '''keyword args'''

# def myfun2(x,y,z):
#     print(f"first {x}")
#     print(f"second {y}")
#     print(f"Third {z}")

# myfun2(y=45,z=23,x=1)    

# def myfun3(b,x,y,z):
#     print(f"1 {b}")
#     print(f"2 {x}")
#     print(f"3 {y}")
#     print(f"4 {z}")
    
# myfun3(56,y=45,z=23,x=1) 
# # myfun3(y=45,z=23,x=1,56)
# print("-----------------------")
# myfun3(56,45,z=23,x=1)  


# """default args"""
# def myfun4(b,x,y="hello",z="jojo"):
#     print(f"1 {b}")
#     print(f"2 {x}")
#     print(f"3 {y}")
#     print(f"4 {z}")

# myfun4(56,45,y="bye",z="om") 
# print("---------------------------")
# myfun4(56,45)     

'''variable length'''
def myfun5(*n):
    sum = 0
    for i in n:
        sum = sum + i
    print(sum)
    
myfun5(2,3,4,5,6)

def myfun6(*n):
    for i in n:
        print(n)

myfun6("hello")

def myfun7(*n,s):
    for i in n:
        print(n,s)
myfun7(22,3,4,5,5,s="hellooooo")