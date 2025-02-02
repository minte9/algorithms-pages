""" Head Permutations

A set is a collection of unique objects {A,B,C}.
Order doesn't matter for a set, {A,B,C} is the same as {B,A,C}
A set like {A,B,C,A} has repeate A and so is not a set.

Head permutations, we place the head in every posible location of the tail.
The permutation of a single char is the char itself (base case).
By putting the B in every possible location of C we get BC CB. 

    BC = None + B + C  # tail[0:0] = None
    CB = C + B + None  # tail[1:]  = None
"""

def head_permutations(chars):

    head = chars[0]  # B
    tail = chars[1:] # C
    prms = []
    for k in range(len(tail) + 1):     
        prms.append(tail[0:k] + head + tail[k:]) 
        
    return prms

print(', '.join(head_permutations('BC')))  # BC, CB
print(', '.join(head_permutations('BCD'))) # BCD, CBD, CDB