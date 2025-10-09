import module6 
import importlib
import time

module6.myfun()
print("------------------")
time.sleep(20)
importlib.reload(module6)
module6.myfun2()

