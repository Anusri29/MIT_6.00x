# Paste your function here
def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    import math
    tt = round(math.sqrt(k*2))
    if k == tt*(tt+1)/2:
        return True
    else:
        return False
