""" Permutations / With repetition
Password checker

The password has exactly 4 chars.
The possible chars are: numbers 2,4,8 and letters J,P,B

These chars can appear more then once:
JPB2, JJJJ, 2442, etc

Each of the six chars can be one of the six posible chars, so
there 6x6x6x = 6^4 = 1296 permutations
"""

def get_permutations_r(str, k, prefix=''):

    if k == 0:
        return [prefix] # Base case

    P = []
    for c in str:
        new_perm = get_permutations_r(str, k-1, prefix + c) # Recursive vase
        P.extend(new_perm)

    return P

print("Permutations with repetition:")
P1 = get_permutations_r('A123', 3)
P2 = get_permutations_r('JPB248', 4)
print(len(P1), "/", ' '.join(P1)) # 64   / AAA AA1 AA2 AA3 A1A 
print(len(P2), "/", ' '.join(P2)) # 1296 / JJJJ JJJP JJJB JJJ2 ...