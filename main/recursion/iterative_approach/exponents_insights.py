""" Calculating exponents
Iterative v2, using insights with power rule from recursive approach.
The generic stack is needed for reversing the order of operations.
(first-in, last-out)
"""

def pow_recursive_v2(x, n):
    if n == 0:
        return 1

    res = pow_recursive_v2(x, n // 2) * \
          pow_recursive_v2(x, n // 2)

    if n % 2 == 0: return res
    if n % 2 == 1: return res * x

def pow_interative_v2(x, n):
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

# Tests
assert pow_interative_v2(2, 1) == 2
assert pow_interative_v2(2, 2) == 4
assert pow_interative_v2(3, 3) == 27
assert pow_interative_v2(3, 5) == 243

# Time
import time
t1 = time.time(); a = pow_interative_v2(3, 600)
t2 = time.time(); b = pow_interative(3, 600)
t3 = time.time(); c = pow_recursive_v2(3, 600)

print("Iterative_v2:", time.time() - t1, 's')
print("Iterative:", time.time() - t2, 's')
print("Recursive_v2:", time.time() - t3, 's')

"""
    Iterative_v2:   0.0003445148468017578 s
    Iterative:      0.0003609657287597656 s
    Recursive_v2:   0.00032448768615722656 s
"""