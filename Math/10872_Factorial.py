x = int(input())

# Solution NOT including recursive function
# for i in range(n):
#     fac*=i+1

# print(fac)

# Solution including recursive function

fac = 1
def factorial(n):
    global fac
    if n<=1:
        return fac 
    fac*=n
    n-=1
    return factorial(n) # The function calls itself as a return value, which is called recursive function.
    #"return factorial(n)", not "factorial(n)". Even it calls itself, it is returning nothing, which python will automatically return 'None', which would make function returning None, not the expected value.
    #https://stackoverflow.com/questions/17778372/why-does-my-recursive-function-return-none

print(factorial(x))