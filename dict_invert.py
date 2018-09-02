# Paste your function here
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    inverted_dict = {}
    for vv in d.values():
        Buffer = []
        for kk in d.keys():
            if d[kk] == vv:
                Buffer.append(kk)
        Buffer.sort()
        inverted_dict[vv] = Buffer
    return inverted_dict

