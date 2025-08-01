'''num = int(input("enter a number "))
num2 = int(input("enter a number "))
lcm =0
big = num if num>num2 else num2 

while True:
    if big%num==0 and big%num2==0:
        lcm = big
        break
    else:
        big +=1


print(lcm)'''

gcd = 0
num1= int(input(" enter num 1 "))
num2= int(input(" enter num 2 "))
i= num1 if num1<num2 else num2
while i>0:
    if num1%i==0 and num2%i==0:
        gcd = i
        break
    else:
        i-=1 
print(gcd)