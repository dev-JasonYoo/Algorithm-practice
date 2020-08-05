# !/user/bin/env python3

# Bubble sort algorithm

def bubblesort(iterable) :
    yet = True
    while yet: # Infinite loop untill sorted ( = untill 'yet == True')
        yet = False # If 'yet' remains 'False', it means they're all sorted
        for index in range(1,len(iterable)) :
            if iterable[index-1] > iterable[index] : # if an element of a lower index is bigger,
                iterable[index-1], iterable[index] = iterable[index], iterable[index-1] # swap them
                yet == True # If 'yet' is 'True', it means they are not yet sorted
