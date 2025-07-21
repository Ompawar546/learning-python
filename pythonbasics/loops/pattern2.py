row = 6
for i in range(1,row+1):
    if i == 1:
        print("*")
    elif i == row:
        print("*"*i)
    else:
        print("*"+" "*(i-2)+"*")        
