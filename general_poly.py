# Paste your function here
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def result(x):
        k = len(L)-1
        a = 0
        for n in L:
            a+= n*x**(k)
            k-=1
        return a
    return result