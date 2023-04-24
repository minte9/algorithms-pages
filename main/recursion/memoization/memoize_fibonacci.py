""" Memoize fibonacci
Memoize the recursive function for specific values that will be 
remembered for future use.
To memoize a function we create a cache dictionary.
"""

import time

cache = {}

def fibonacci_recursive(n):
    if n == 1: return 1
    if n == 2: return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_memoize(n):
    global cache

    if n == 1: cache[n] = 1; return 1
    if n == 2: cache[n] = 1; return 1
    if n in cache:
        return cache[n]

    res = fibonacci_memoize(n-1) + fibonacci_memoize(n-2)
    cache[n] = res
    return res

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

fibonacci_memoize(100) = 354224848179261915075      0.0005996227264404297 s
fibonacci_recursive(36) = 14930352                  4.443222761154175 s
fibonacci_iterative(100) = 354224848179261915075    1.430511474609375e-05 s

"""