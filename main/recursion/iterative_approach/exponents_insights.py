""" Calculating exponents
Iterative v2, using insights with power rule from recursive approach.
The generic stack is needed for reversing the order of operations.
(first-in, last-out)
"""

import time

def pow_recursive_v2(x, n):
    if n == 0:
        return 1

    res = pow_recursive_v2(x, n // 2) * pow_recursive_v2(x, n // 2) # floor division

    if n % 2 == 0: # even
        return res
    elif n % 2 == 1: # odd
        return res * x

def pow_interative_v2(x, n): # Iterative
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

def pow_interative(x, n): # Iterative
    res = x
    for i in range(1, n):
        res = res * x
    return res

assert pow_interative_v2(2, 1) == 2
assert pow_interative_v2(2, 2) == 4
assert pow_interative_v2(3, 3) == 27
assert pow_interative_v2(3, 5) == 243

start = time.time()
a = pow_interative_v2(3, 600)
print("Iterative_v2: \t", time.time() - start, 'sec')

start = time.time()
b = pow_interative(3, 600)
print("Iterative: \t", time.time() - start, 'sec')

start = time.time()
c = pow_recursive_v2(3, 600)
print("Recursive_v2: \t", time.time() - start, 'sec')

# Iterative_v2:    6.4373016357421875e-06 sec
# Iterative:       5.0067901611328125e-05 sec
# Recursive_v2:    0.0003235340118408203 sec