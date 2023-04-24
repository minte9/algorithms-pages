""" Calculating exponents x^n

Iterative, a loop that repeatedly multiplies a number by itself
    res = res * x
Recursive, use the power rule: 
    a^n = a^(n-1) * a^1 
Recursive v2, each call cuts the problem in half: 
    a^6 = a^3 * a^3
    a^5 = a^2 * a^2 * a
"""

import time

def pow_interative(x, n): # Iterative
    res = x
    for i in range(1, n):
        res = res * x
    return res

def pow_recursive(x, n):
    if n == 0: 
        return 1 # Base case
    res = pow_recursive(x, n-1) * x
    return res

def pow_recursive_v2(x, n):
    if n == 0:
        return 1

    res = pow_recursive_v2(x, n // 2) * pow_recursive_v2(x, n // 2) # floor division

    if n % 2 == 0: # even
        return res
    elif n % 2 == 1: # odd
        return res * x

assert pow_interative(2, 2) == 4
assert pow_interative(3, 3) == 27
assert pow_recursive(2, 2) == 4
assert pow_recursive(3, 3) == 27
assert pow_recursive(2, 2) == 4
assert pow_recursive(3, 3) == 27

start = time.time()
a = pow_interative(3, 600)
print("Iterative: \t", time.time() - start, 'sec') 
    # 5.221366882324219e-05 sec

start = time.time()
b = pow(3, 600)
print("Native: \t", time.time() - start, 'sec') 
    # 0.0000003 sec

start = time.time()
c = pow_recursive(3, 600)
print("Recursive: \t", time.time() - start, 'sec') 
    # 0.0004 sec

start = time.time()
d = pow_recursive_v2(3, 600)
print("Recursive_v2: \t", time.time() - start, 'sec') 
    # 0.0003 sec