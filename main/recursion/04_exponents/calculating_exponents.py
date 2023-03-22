""" Calculating exponents x^n

Iterative, a loop that repeatedly multiplies a number by itself
    res = res * x

Recursive, use the power rule: 
    a^n = a^(n-1) * a^1 

Recursive v2, each call cuts the problem in half: 
    a^6 = a^3 * a^3
    a^5 = a^2 * a^2 * a
"""

# Iterative
def ipow(x, n):
    res = x
    for i in range(1, n):
        res = res * x
    return res

# Recursive
def rpow(x, n):
    if n == 0: 
        return 1 # base case
    res = rpow(x, n-1) * x # recursive case
    return res

# Recursive (v2)
def rpow2(x, n):
    if n == 0:
        return 1
    res = rpow2(x, n // 2) * rpow2(x, n // 2) # floor division
    if n % 2 == 0: # even
        return res
    elif n % 2 == 1: # odd
        return res * x

# Tests
assert ipow(2, 2)  == 4
assert ipow(3, 3)  == 27

assert rpow(2, 2)  == 4
assert rpow(3, 3)  == 27
assert rpow2(2, 2) == 4
assert rpow2(3, 3) == 27


# Limits
import time

# Iterative
start = time.time(); a = ipow(3, 600)
print("Iterative: \t", time.time() - start, 'sec') 
    # 5.221366882324219e-05 sec

# Native
start = time.time(); b = pow(3, 600)
print("Native: \t", time.time() - start, 'sec') 
    # 0.0000003 sec

# Recursive
start = time.time(); c = rpow(3, 600)
print("Recursive: \t", time.time() - start, 'sec') 
    # 0.0004 sec

# Recursive (v2)
start = time.time(); d = rpow2(3, 600)
print("Recursive_v2: \t", time.time() - start, 'sec') 
    # 0.0003 sec