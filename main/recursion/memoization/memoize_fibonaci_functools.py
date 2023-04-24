""" Memoize fibonacci - functools
Python standard library has a function decorator lru_cache() 
that automatically memoize the function it decorates.
Memoization can be apply to any pure function to speed up the execution.
"""

import time
import functools

def fibonacci_recursive(n):
    if n == 1: return 1
    if n == 2: return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

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


start = time.time()
n = fibonacci_memoize(100)
print("fibonacci_memoize(100)  =", n, time.time() - start, 's') 

start = time.time()
n = fibonacci_recursive(36)
print("fibonacci_recursive(36) =", n, time.time() - start, 's') 

start = time.time()
n = fibonacci_iterative(100)
print("fibonacci_iterative(100) =", n, time.time() - start, 's') 

"""

fibonacci_memoize(100)   = 354224848179261915075    0.00023746490478515625 s
fibonacci_recursive(36)  = 14930352                 4.304527521133423 s
fibonacci_iterative(100) = 354224848179261915075    1.1682510375976562e-05 s

"""