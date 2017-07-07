def getMaxElement(L1):
    d = {L1.count(x):x for x in L1}
    countMax = max(d.keys())

    countMax_element = d[max(d.keys())]
    typeOfElement = type(countMax_element)

    A = []
    A.append(countMax_element)
    A.append(countMax)
    A.append(typeOfElement)
    return tuple(A)

def listArg(L, element):
    '''
    Gives the argument of the first occurance of an element
    '''
    count = 0
    for ll in L:
        if element == ll:
            return count
        count += 1
    if count >= len(L):
        return None

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
    If they are permutations of each other, returns a
    tuple of 3 items in this order:
    the element occurring most, how many times it occurs, and its type
    '''
    L2_copy = L2
    if (len(L1) - len(L2))**(len(L1)*len(L2)) == 0:
        for element in L1:
            if element in L2:
                arg = listArg(L2, element)
                L2_copy.pop(arg) 
        if len(L2_copy) == 0:
            return getMaxElement(L1)
        else:
            return False
    else:
        if len(L1)+len(L2) == 0: return (None, None, None)
        return False

