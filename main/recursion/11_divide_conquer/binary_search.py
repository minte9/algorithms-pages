""" Binary search
Works only if the list is sorted.
A linear search of a shelf with 100 books takes 100 steps.
A binary search on 50 takes 6 and on 100 only 7 steps.

Notice, the code performs no action after the recursive call.
It means that the binary search can be easily implemented iteratively.

Params: left and right indexes of the search range
Process: the range half in size for each recursive call
Base case: when the haystack has only one item
"""

def binary_search(needle, haystack, left=None, right=None):

    # Defaults
    if left == None: # first in haystack
        left = 0   
        
    if right == None: # last in haystack
        right = len(haystack) - 1

    middle = (left + right) // 2

    if needle == haystack[middle]: # Base case
        return middle

    if left > right: # Base case
        return None

    if needle < haystack[middle]:
        return binary_search(needle, haystack, left, middle - 1) # Recursive

    if needle > haystack[middle]:
        return binary_search(needle, haystack, middle + 1, right) # Recursive


def ibinary_search(needle, haystack, left=None, right=None):
    
    # Defaults
    if left == None: # first in haystack
        left = 0   

    if right == None: # last in haystack
        right = len(haystack) - 1

    while True:
        middle = (left + right) // 2

        if needle == haystack[middle]:
            return middle

        if left > right:
            return None

        if needle < haystack[middle]:
            right = middle - 1
        
        if needle > haystack[middle]:
            left = middle + 1


data = [1, 4, 8, 11, 13, 16, 19, 19]

# Recursive
assert binary_search(1, data)   == 0
assert binary_search(19, data)  == 6
assert binary_search(100, data) == None

# Iterative
assert ibinary_search(1, data)   == 0
assert ibinary_search(19, data)  == 6
assert ibinary_search(100, data) == None

print("Tests passed")