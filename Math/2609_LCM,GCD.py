#!/usr/bin/env python
#No.2609
#Memory: 29200KB
#Time: 27ms
#Length: 595B

a,b = map(int,input().split(" "))
big_int = max(a,b)
factor = []
lcm,gcd = 1,1


def is_factor(n,m): #determine whether n is a factor of m
    if m%n == 0:
        return True
    else:
        return False

while True:
    for i in range(2,big_int+1):
        while is_factor(i,a) and is_factor(i,b):
            a,b = a/i,b/i
            factor.append(i)
        if i>=max(a,b):
            while_break=True
            break
    if while_break==True or a*b == 1: #handling an exception when 'a' and 'b' is both 1
        break

for i in range(len(factor)):
    lcm *= factor[i]

gcd = int(lcm*a*b)

print(lcm,gcd,sep="\n")