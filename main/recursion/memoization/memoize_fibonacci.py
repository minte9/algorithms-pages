""" Memoize fibonacci
Memoize the recursive function for specific values that will be 
remembered for future use.
To memoize a function we create a cache dictionary.
"""

def fibonacci_recursive(n):
    if n == 1: return 1
    if n == 2: return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

CACHE = {}
def fibonacci_memoize(n):
    global CACHE

    if n == 1: CACHE[n] = 1; return 1
    if n == 2: CACHE[n] = 1; return 1
    if n in CACHE:
        return CACHE[n]

    res = fibonacci_memoize(n-1) + fibonacci_memoize(n-2)
    CACHE[n] = res
    return res

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
    fibonacci_memoize(100) 2.7990965843200684 s
    fibonacci_recursive(36) 2.7989842891693115 s
    fibonacci_iterative(100) 4.982948303222656e-05 s
"""