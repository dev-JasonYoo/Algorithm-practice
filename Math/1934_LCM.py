def is_factor(n,m): #determine whether n is a factor of m
    if m%n == 0:
        return True
    else:
        return False

def gcd(a,b):
    big_int = max(a,b)
    factor = []
    lcm,gcd = 1,1
    
    while True:
        for i in range(2,big_int+1):
            while is_factor(i,a) and is_factor(i,b):
                a,b = a/i,b/i
                factor.append(i)
            if i>=max(a,b):
                while_break=True
                break
        if while_break==True or a*b == 1:
            break

    for i in range(len(factor)):
        lcm *= factor[i]
    
    gcd = int(lcm*a*b)

    return gcd

t = int(input())
num = []

for i in range(t):
    num.append(list(map(int,input().split(" "))))

for i in range(t):
    print(gcd(num[i][0], num[i][1]))