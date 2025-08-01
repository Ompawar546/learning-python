"""i=0
while i<10:
    print(i,end=" ")
    i+=1"""

"""i=0
j= "HELLO"
while i<len(j):
    k = ord(j[i])
    print(chr(k+32),end="")
    i+=1
"""
x= [22,45,34,56,55,35.60,34.67,32.32,77,67,88,80,89,56,"om"]
j=0
while j<len(x):
    if isinstance(x[j],(int,float)):
        if x[j]%2==0:
            print(x[j])
    
    j+=1
