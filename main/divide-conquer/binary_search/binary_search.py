""" Binary search / Algorithm
Binary search works only for ordered lists key search.

A linear search of a shelf with 100 books takes 100 steps.
A binary search on 50 takes 6 and on 100 only 7 steps.
"""

import sys
sys.dont_write_bytecode = True # import custom module
from decorators import timer

@timer 
def binary_search(needle, haystack):
    i = 0 
    j = len(haystack) - 1

    while True:
        m = (i + j) // 2
        if needle > haystack[m]:  i = m + 1
        if needle < haystack[m]:  j = m - 1
        if needle == haystack[m]: 
            return m
        if i > j: 
            return None

@timer
def linear_search(needle, haystack):
    for i in range(len(haystack)):
        if needle == haystack[i]:
            return i
    return None

@timer
def generate_data():
    data = [i for i in range(123456789)]
    return data

# Tests
data = [1, 4, 8, 11, 13, 16, 19, 19]
assert binary_search(1, data)   == 0
assert binary_search(19, data)  == 6
assert binary_search(100, data) == None
print("Tests passed")

# Time
lst = generate_data()
key = binary_search(123456780, lst)
key = linear_search(123456780, lst)

"""
    generate_data() time:    5.986196041107178 s
    binary_search() time:    1.8835067749023438e-05 s
    linear_search() time:    8.184731483459473 s
"""