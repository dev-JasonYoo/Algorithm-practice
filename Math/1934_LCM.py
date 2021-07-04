#!/usr/bin/env python
#No.1934
#Memory: 29452KB
#Time: 160ms
#Length: 272B


def euc_lcm(a,b): #Returns LCM of 'a' and 'b' by Euclidean Algorithm
    if a%b == 0 :
        return b
    return euc_lcm(b,a%b)

def gcd(a,b):
    return int(a*b/euc_lcm(a,b))

t = int(input())

while t:
    a,b=map(int,input().split(" "))
    print(gcd(a,b))
    t -= 1