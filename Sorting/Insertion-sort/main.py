# !/usr/bin/env python3

# Insertion sort algorithm
# reference: https://lamfo-unb.github.io/2019/04/21/Sorting-algorithms/

def insertsort(iterable) :
    for current in range(1,len(iterable)) : # iterable[0] is consdiered as resorted in the beginning
        current_value = iterable[current] # saving current value
        compare = current
        while 0 < compare and iterable[compare-1] > current_value : # finding out where to put the sorted current value
            iterable[compare] = iterable[compare-1] # this line in the while loop moves the elements not sorted
            compare -= 1 

        iterable[compare] = current_value # put current value into the right place that the while loop found out


    return(iterable)
