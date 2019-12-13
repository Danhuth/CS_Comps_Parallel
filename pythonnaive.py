import numpy as np

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func
def L(n,S):
    if n == 0:
        return np.array([0])
    elif n < min(S):
        return np.array([])
    else:
        lengths = np.array([])
        for a in S:
            new_length =np.array([x+1 for x in L(n-a,S)])     #gets the same list of components, but uses numpy to get unique values
            lengths = np.union1d(new_length, lengths)
        return lengths
L = memoize(L)

def delta(l):
    lengths = sorted(list(l))
    delta_set = set([])
    for i in range(len(lengths)-1):
        delta_set = delta_set.union({lengths[i+1] - lengths[i]})
    return delta_set

def delta_set_bound(S,bound):
    delta_set = set([])
    for n in range(bound):
        delta_set = delta_set.union(delta(L(n,S)))
    return delta_set