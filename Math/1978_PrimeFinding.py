t = int(input())

num = list(map(int,input().split(" ")))

def is_prime(n):
    for i in range(2,n//3+1):
        if n%i == 0:
            return 0 # returned value '0' means that it is NOT a prime number
    if n == 1 or n == 4: # exception handling when n is 1 or 4
        return 0 # 1 is NOT a prime number
    
    return 1 # returned value '1' means that it is a prime number

count = 0
for i in range(len(num)):
    if is_prime(num[i]):
        count += 1

print(count)