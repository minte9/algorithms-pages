""" Head Permutations
We select the first element from the set as the head.
We get all the permutations from the rest of elements (the tail).
For each permutation we place the head in every posible location.

The permutation of a single char is the char itself (base case).
By putting the B in every possible location of C we get BC CB. 

 BC = None + B + C  # tail[0:0] = None
 CB = C + B + None  # tail[1:]  = None
"""

def head_permutations(chars):
    if len(chars) == 1:
        return [chars] # Base case

    head = chars[0]  # B
    tail = chars[1:] # C
    prms = []
    for k in range(len(tail) + 1):     
        prms.append(tail[0:k] + head + tail[k:]) 
        
    return prms

print(', '.join(head_permutations('BC'))) # BC, CB
print(', '.join(head_permutations('ABC'))) # ABC, BAC, BCA