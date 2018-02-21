"""
Different sorting functions
authors: Luc Blassel, Romain Gautron
"""

def shellSort(array,dim):
    "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
    gap = len(array) // 2
    # loop over the gaps
    while gap > 0:
        # do the insertion sort
        for i in range(gap, len(array)):
            val = array[i][dim]
            j = i
            while j >= gap and array[j - gap][dim] > val:
                array[j][dim] = array[j - gap][dim]
                j -= gap
            array[j][dim] = val
        gap //= 2
    return array
