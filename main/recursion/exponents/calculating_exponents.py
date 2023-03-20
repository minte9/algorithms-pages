""" Calculating exponents
Iterative, create a loop that repeatedly multiplies a number by itself
Recursive, uses the power rule: a^(n) x a^(1) = a^(n+1)

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
    n = n - 1
    return x * rpow(x, n) # recursive case

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

start = time.time()
a = ipow(3, 600)
print("Iterative: \t", time.time() - start, 'sec') # 5.221366882324219e-05 sec

start = time.time()
b = pow(3, 600)
print("Native: \t", time.time() - start, 'sec') # 3.337860107421875e-06 sec

start = time.time()
c = rpow(3, 600)
print("Recursive: \t", time.time() - start, 'sec') # 0.0004024505615234375 sec

start = time.time()
d = rpow2(3, 600) # recursive v2
print("Recursive_v2: \t", time.time() - start, 'sec') # 0.0003349781036376953 sec