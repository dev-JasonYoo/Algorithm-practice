import sys

sys.setrecursionlimit(10**7)

t = int(input())

for _ in range(t):
    x = int(input())
    fac = 1
    def factorial(n): #recursive function finding factorial
        global fac
        if n<=1:
            return fac
        fac*=n
        return factorial(n-1)

    def factorial_len(n): #function finding the number of digits of factorial of n.
        li = list(str(factorial(n))) #ex) list(str(120)): [1,2,0]
        print(len(li))
    
    factorial_len(x)