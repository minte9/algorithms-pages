""" Binary search - Key search algorithm for ordered lists

A linear search of a shelf with 100 books takes 100 steps.
A binary search on 50 takes 6 and on 100 only 7 steps.
"""

def binary_search(needle, haystack):

    i, j = 0, len(haystack) - 1

    while True:
        m = (i + j) // 2

        if needle > haystack[m]:  i = m + 1
        if needle < haystack[m]:  j = m - 1
        if needle == haystack[m]: 
            return m # found item, return key

        if i > j: 
            return None # break loop


data = [1, 4, 8, 11, 13, 16, 19, 19]
assert binary_search(1, data)   == 0
assert binary_search(19, data)  == 6
assert binary_search(100, data) == None
print("Tests passed")