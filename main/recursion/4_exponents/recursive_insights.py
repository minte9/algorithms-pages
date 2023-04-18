""" Calculating exponents
Iterative v2, using insights with power rule from recursive approach.
The generic stack is needed for reversing the order of operations.
(first-in, last-out)
"""

# Recursive (v2)
def rpow2(x, n):
    if n == 0:
        return 1
    res = rpow2(x, n // 2) * rpow2(x, n // 2) # floor division
    if n % 2 == 0: # even
        return res
    elif n % 2 == 1: # odd
        return res * x

# Iterative (v2)
def ipow2(x, n):
    operations = []
    while n > 1:
        if n % 2 == 0:
            operations.append('square')
            n = n // 2 
        elif n % 2 == 1:     
            operations.append('multiply')
            n = n - 1
    res = x
    while operations:
        op = operations.pop()
        if op == 'square':
            res = res * res
        elif op == 'multiply':
            res = res * x

    return res

# Tests
assert ipow2(2, 1) == 2
assert ipow2(2, 2) == 4
assert ipow2(3, 3) == 27
assert ipow2(3, 5) == 243

# Limits
import time

start = time.time()
d = rpow2(3, 600) # recursive v2
print("Recursive_v2: \t", time.time() - start, 'sec') # 0.0003349781036376953 sec

start = time.time()
e = ipow2(3, 600)
print("Iterative_v2: \t", time.time() - start, 'sec') # 1.0728836059570312e-05 sec