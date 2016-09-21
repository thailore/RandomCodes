from itertools import combinations

#find all subsequences of string s

#created combinations, then created set of that

def subsequences(s):
    """Returns set of all subsequences in s."""
    return set(''.join(c) for i in range(len(s) + 1) for c in combinations(s, i))
