# Paste your function here
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # Your code here
    odd_count= []

    for ii in L:
        if (L.count(ii)) %2 != 0:
            odd_count.append(ii)

    if len(odd_count)>0:
        return max(odd_count)
    else:
        return None

