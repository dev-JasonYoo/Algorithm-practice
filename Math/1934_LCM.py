#!/usr/bin/env python
#No.1934
#Memory: 29452KB
#Time: 160ms
#Length: 272B


def euc_gcd(a,b): #Returns GCD of 'a' and 'b' by Euclidean Algorithm
    if a%b == 0 :
        return b
    return euc_gcd(b,a%b)

def lcm(a,b):
    return int(a*b/euc_gcd(a,b))

t = int(input())

while t:
    a,b=map(int,input().split(" "))
    print(lcm(a,b))
    t -= 1