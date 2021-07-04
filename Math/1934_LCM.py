#!/usr/bin/env python
#No.1934
#Memory: 29452KB
#Time: 112ms
#Length: 370B


def euc_lcm(a,b): #Returns LCM of 'a' and 'b' by Euclidean Algorithm
    if a<b:
        a,b = b,a
    if a%b == 0 :
        return b
    a = a%b
    return euc_lcm(a,b)

def gcd(a,b):
    return int(a*b/euc_lcm(a,b))

t = int(input())
num = []

for i in range(t):
    num.append(list(map(int,input().split(" "))))

for i in range(t):
    print(gcd(num[i][0],num[i][1]))