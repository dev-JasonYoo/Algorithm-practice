# !/usr/bin/env python3

'''
How to use:

Enter the following:
(texts to be put) (overall format)

The space between the two is mandatory to distinguish them.

@ in overall format represents the place to be changed.

Overall format can have a prefix and a suffix.

ex)
input : 12345 0000@@a
output: 000001a, 000002a, 000003a, ... , 000053a, 000054a, 000055a

Given the length of the texts to be put is 'i' and the length of the places to be changed(@) is 'n',
the total number of passwords in the list is i^n.

'''

raw = input()
data = raw.split(' ') # data[0] ==> texts to be put, data[1] ==> overall format
result1 = []

# 'n' represents the number of @, the places to be alternated by the given text.
n = 0
for num in range(len(data[1])) :
    if data[1][num] == '@' :
        n += 1

count = 2 # 'count' represents the total time of ongoing loop, which is to be 'n' at the last loop.
def change() :
    i = 0
    j = 0
    global count
    # globals() function returns the dictionary of a global symbol table, a data structure which contains all necessary information about the program.
    globals()['result{}'.format(count)] = [] # assign a new list 'result n'
    
    for i in range(len(globals()['result{}'.format(count-1)])) : # refers n-1th list to fill nth list
        for j in range(len(data[0])) : # alternate nth '@' by the given text
            globals()['result{}'.format(count)].append(globals()['result{}'.format(count-1)][i].replace('@', data[0][j],1))

    count += 1

# First loop : fills the list 'result1' with i^1 elements.
# First @ is alternated.
for i in range(len(data[0])) :
    result1.append(data[1].replace('@', data[0][i],1))

# nth loop : starting from the second loop. Each nth loop fills the list 'result n' with i^n elements.
# nth @ is alternated.
for k in range(n-1) :
    change()

print(globals()['result{}'.format(n)])
