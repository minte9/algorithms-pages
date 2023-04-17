""" Binary search - Key search algorithm for ordered lists

A linear search of a shelf with 100 books takes 100 steps.
A binary search on 50 takes 6 and on 100 only 7 steps.
"""

import time
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + "()", "time:\t", end - start, "s")
        return result
    return wrapper

@timer_decorator
def linear_search(needle, haystack):
    for i in range(len(haystack)):
        if needle == haystack[i]:
            return i
    return None

@timer_decorator
def binary_search(needle, haystack):

    i, j = 0, len(haystack) - 1

    while True:
        m = (i + j) // 2

        if needle > haystack[m]:  i = m + 1
        if needle < haystack[m]:  j = m - 1
        if needle == haystack[m]: return m
        if i > j: return None

@timer_decorator
def generate_data():
    data = [i for i in range(123456789)] # list comprehension
    return data

data = generate_data()
key = linear_search(123456780, data)
key = binary_search(123456780, data)

"""
generate_data() time:    5.557476043701172 s
linear_search() time:    7.532944917678833 s
binary_search() time:    1.6689300537109375e-05 s
"""