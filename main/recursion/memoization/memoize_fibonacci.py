""" Memoize fibonacci
Memoize the recursive function for specific values that will be 
remembered for future use.
To memoize a function we create a cache dictionary.
"""

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

# Time
import time
t1 = time.time(); n = fibonacci_memoize(100)
t2 = time.time(); n = fibonacci_recursive(36)
t3 = time.time(); n = fibonacci_iterative(100)

print("fibonacci_memoize(100)", time.time() - t1, 's') 
print("fibonacci_recursive(36)", time.time() - t2, 's') 
print("fibonacci_iterative(100)", time.time() - t3, 's') 

"""
    fibonacci_memoize(100) 2.627922773361206 s
    fibonacci_recursive(36) 2.627795934677124 s
    fibonacci_iterative(100) 7.200241088867188e-05 s
"""