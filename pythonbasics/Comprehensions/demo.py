#create a list with even no from existing list without using Comprehnsion
x = [1,2,3,4,5,6,7,8,9]
y=[]
for i in x:
    if i%2==0:
        y.append(i)
print(y)        

#with using comprehension
z = [i for i in x if i%2==0]
print(z)