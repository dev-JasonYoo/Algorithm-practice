def bubblesort(iterable) :
    while True: # Infinite loop untill sorted
        count = 1 # If for-loop is not executed, count remains 1, which means that it's all sorted and leads to break.
        for index in range(1,len(iterable)) :
            if iterable[index-1] > iterable[index] : # if an element of a lower index is bigger,
                iterable[index-1], iterable[index] = iterable[index], iterable[index-1] # swap them
                count *= 0 # 'count == 0' means 'not sorted yet'
        if count == 1 : # 'count == 1' means 'all sorted'
            break
