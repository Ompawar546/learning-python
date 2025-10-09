from random import *
from string import *

print(ascii_letters)
print(ascii_lowercase)
print(ascii_uppercase)
print(punctuation)


def pwd(p=8):
    coll = ascii_letters + digits + punctuation
    res = choices(coll,k=p)
    op = "".join(res)
    return op

print("--------------password---------------")
print(pwd(p=10))





# print(random())

# print(randint(1000,9999))

# print(randrange(3,500,3))

