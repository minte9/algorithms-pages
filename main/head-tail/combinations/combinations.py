""" K-Combinations
Generating all k-combinations of a set is a bit tricky.

You don't want your algorithm to generatate duplicates.
For AB 2-combination from a set {A,B,C} you don't want also create BA, 
because is the same 2-combination as AB

When k=0 we need to return a list containing a single empty string.
Otherwise the C1 will return an empty list.

When s='' we return an empty list so that both C1 and C2 recursive cases 
will return an empty list.
"""

def combinations(s, k):

    if k == 0: return [''] # Base case
    if s == '': return [] # Base case

    head = s[:1]
    tail = s[1:]
    
    # Combintations that include the head
    C1 = [head + c for c in combinations(tail, k-1)]

    # Combinations without the head
    C2 = combinations(tail, k)

    return C1 + C2

print("K-Combinations:")
print(' '.join(combinations('ABC', 2)))  # AB AC BC
print(' '.join(combinations('ABCD', 3))) # ABC ABD ACD BCD  