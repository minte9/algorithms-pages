""" Memoize fibonacci - functools
Python standard library has a function decorator lru_cache() 
that automatically memoize the function it decorates.
Memoization can be apply to any pure function to speed up the execution.
"""

def fibonacci_recursive(n):
    if n == 1: return 1
    if n == 2: return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

import functools # Look Here
@functools.lru_cache()
def fibonacci_memoize(n):
    if n == 1: return 1
    if n == 2: return 1
    return fibonacci_memoize(n-1) + fibonacci_memoize(n-2)

def fibonacci_iterative(n):
    a, b = 1, 1
    for i in range(1, n-1):
        a, b = b, a + b
    return b

# Tests
assert fibonacci_iterative(2) == 1
assert fibonacci_iterative(3) == 2
assert fibonacci_recursive(4) == 3
assert fibonacci_recursive(5) == 5
assert fibonacci_memoize(6) == 8
assert fibonacci_memoize(7) == 13

# Time
import time
t1 = time.time(); n = fibonacci_memoize(100)
t2 = time.time(); n = fibonacci_recursive(36)
t3 = time.time(); n = fibonacci_iterative(100)

print("fibonacci_memoize(100)", time.time() - t1, 's') 
print("fibonacci_recursive(36)", time.time() - t2, 's') 
print("fibonacci_iterative(100)", time.time() - t3, 's') 

"""
    fibonacci_memoize(100) 2.659872531890869 s
    fibonacci_recursive(36) 2.6597554683685303 s
    fibonacci_iterative(100) 5.054473876953125e-05 s
"""