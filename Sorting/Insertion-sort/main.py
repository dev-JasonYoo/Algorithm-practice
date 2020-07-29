# !/usr/bin/env python

# Insertion sort algorithm
# Since made without any guide, this algorithm may not be the most efficient for insertion sort

def insertsort(iterable) :
    
    for current in range(len(iterable)) : # 'current' is the index of the element being sorted

        compare, n = 0,0 # Initializes 'compare' and 'n' which is used in for-loop in each current for-loop
        current_value = iterable[current] # Saves the element being sorted since the corresponding space will be assigned by the leading value
        
        for compare in range(0,current) : # Compares the element from [0] to the element right ahead of [current]            
            if not iterable[compare] < iterable[current] : # Finds where to insert 'current_value,' stored value of [current]

                for n in range(current,compare,-1) : # Translate the values to one space to make the space where 'current_value' will be put empty
                    iterable[n] = iterable[n-1]
                    
                iterable[compare] = current_value # Insert the saved value of [current] to the right place
                
    return(iterable)
