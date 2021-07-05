import sys
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)): # not 'sqrt(n)' but 'sqrt(n)+1' because it should determine values to sqrt(n) whether is prime. (the lastest test value should be sqrt(n).)
        if n%i == 0:
            return 0 # returned value '0' means that it is NOT a prime number
    if n == 1 or n == 4: # exception handling when n is 1 or 4
        return 0 # 1 is NOT a prime number
    
    return 1 # returned value '1' means that it is a prime number

num=[]
while True:
    num.append(int(sys.stdin.readline())) # instead of using input(), you should use sys.stdin.readline() which is faster
    if not num[-1]: # when the input is zero
        break

for i in range(len(num)-1): #Exculded caculating the last '0'(n[-1])
    for j in range(3,num[i]//2+1,2): # need to calculate only to num[i]//2 since the next values are already reviewed
        if is_prime(j) and is_prime(num[i]-j): # when both are prime numbers
            print(f"{num[i]} = {j} + {num[i]-j}")
            break
        if j == num[i]//2:
            print("Goldbach's conjecture is wrong.")