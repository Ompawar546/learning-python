l= [34,56,13,17,45,78]
for i in l:
   for x in range(2,i):
       if i==0 or i==1:
        print("none")
        break
       elif i%x==0:
        print("not a prime")
        break
       else:
        print("is a prime")
        break 
       