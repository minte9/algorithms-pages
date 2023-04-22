""" Permutations / Without repetition

We select one of the elements from the set as the head.
We get all the permutations from the rest of elements (the tail).
For each permutation we place the head in every posible location.

The permutation of a single char is the char itself (base case).
By putting the B in every possible location of C we get BC CB. 
"""

def get_permutations(chars):
    
    if len(chars) == 1:
        return [chars] # C

    head = chars[0]  # A
    tail = chars[1:] # BC
    tail_prms = get_permutations(tail) # C / BC CB

    prms = []
    for tail in tail_prms:
        for k in range(len(tail) + 1):
            prms.append(tail[0:k] + head + tail[k:])

    return prms # BC CB

print("Permutations without repetition:")
P1 = get_permutations('ABC')
P2 = get_permutations('ABCD')
print(len(P1), ' '.join(P1)) # 6  ABC BAC BCA ACB CAB CBA
print(len(P2), ' '.join(P2)) # 24 24 ABCD BACD BCAD BCDA ACBD ...
