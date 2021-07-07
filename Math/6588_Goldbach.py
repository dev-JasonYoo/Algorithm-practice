import sys
import math

t = 100001

def prime_list(t): # makes a list of boolean each of which value states whether corresponding value is a prime number (True: Prime, False: Not prime)
    global is_prime_list
    is_prime_list=[False,False]+[True]*(t-1) # List multiplication is the fastest method to create a list (https://stackoverflow.com/questions/8936294/why-is-append-slower-than-setting-the-value-in-a-pre-allocated-array/8936380, https://stackoverflow.com/questions/20816600/best-and-or-fastest-way-to-create-lists-in-python)
    for i in range(t+1):
        #is_prime_list.append(bool(is_prime(i))) # rather than append() method,
        is_prime_list[i] = is_prime(i) # pre-allocate the list by list multiplication and then change the elements (p.s. however the calculation time didn't change although I changed to pre-allocating algorithm. Still couldn't figure out the reason)

def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)): # not 'sqrt(n)' but 'sqrt(n)+1' because it should determine values to sqrt(n) whether is prime. (the lastest test value should be sqrt(n).)
        if n%i == 0:
            return 0 # returned value '0' means that it is NOT a prime number
    if n == 1 or n == 4: # exception handling when n is 1 or 4
        return 0 # 1 is NOT a prime number
    
    return 1 # returned value '1' means that it is a prime number

# num=[2*x for x in range(t//2)] # Code for debugging
while True:
    num.append(int(sys.stdin.readline())) # instead of using input(), you should use sys.stdin.readline() which is faster
    if not num[-1]: # when the input is zero
        break

prime_list(t)
#The following for loop is used when function "prime_list(t)" is used
for i in range(len(num)): #Exculded caculating the last '0'(n[-1])
    for j in range(3,num[i]//2+1,2): # need to calculate only to num[i]//2 since the next values are already reviewed
        try:
            if is_prime_list[j] and is_prime_list[num[i]-j]: # when both are prime numbers
                print("{} = {} + {}".format(num[i],j,num[i]-j))
                break
            if j == num[i]//2:
                print("Goldbach's conjecture is wrong.")
                
        except IndexError: # Code for debugging
            print("IndexError: j = ", j)


            
#The following for loop is used when function "prime_list(t)" is NOT used
# for i in range(len(num)-1): #Exculded caculating the last '0'(n[-1])
#     for j in range(3,num[i]//2+1,2): # need to calculate only to num[i]//2 since the next values are already reviewed
#         if is_prime_list[j] and is_prime_list[num[i]-j]: # when both are prime numbers
#             print("{} = {} + {}".format(num[i],j,num[i]-j))
#             break
#         if j == num[i]//2:
#             print("Goldbach's conjecture is wrong.")