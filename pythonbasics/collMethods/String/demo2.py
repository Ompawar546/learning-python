s="There are some late commers in class"
i=-1
'''for i in range(0,len(s)):
    if s[i]=="e":
        print(i)
'''

while True:
    i=s.find("e",i+1,len(s)-1)
    if i == -1:
        break
    print(i)

    

'''print(s.find("o"))
print(s.index("o"))
print(s.rfind("o"))
print(s.rindex("o"))
print(s.find("z"))
print(s.rfind("z"))'''



'''print(s.find("e",2))
print(s.index("e",2))
'''










'''j=0
k=-len(s)+1
i=0
print(k)
while i>k:
    if s[k]=="e":
        print(j)
        break
    else:
        k-=1 
'''

'''while True:
    if s[j]=="o":
        print(j)
        break
    else:
        j+=1    
    '''