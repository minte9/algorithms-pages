""" Calculating exponents: x^n

Iterative, a loop that repeatedly multiplies a number by itself
    res = res * x

Recursive, use the power rule: 
    a^n = a^(n-1) * a^1 
    
Recursive v2, each call cuts the problem in half: 
    a^6 = a^3 * a^3
    a^5 = a^2 * a^2 * a
"""

def pow_interative(x, n):
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

    res = pow_recursive_v2(x, n // 2) * \
          pow_recursive_v2(x, n // 2)

    if n % 2 == 0: return res
    if n % 2 == 1: return res * x

def native_pow(x, n):
    return pow(x, n)

# Tests
assert pow_interative(2, 2) == 4
assert pow_interative(3, 3) == 27
assert pow_recursive(2, 2) == 4
assert pow_recursive(3, 3) == 27
assert pow_recursive(2, 2) == 4
assert pow_recursive(3, 3) == 27

# Time
import time
t1 = time.time(); result = pow_interative(3, 600)
t2 = time.time(); result = pow_recursive(3, 600)
t3 = time.time(); result = pow_recursive_v2(3, 600)
t4 = time.time(); result = native_pow(3, 600)

print("Iterative pow: \t", time.time() - t1, 's') 
print("Recursive pow: \t", time.time() - t2, 'sec') 
print("Recursive_v2: \t", time.time() - t3, 'sec') 
print("Native pow: \t", time.time() - t4, 's') 

"""
    Iterative pow:   0.0007915496826171875 s
    Recursive pow:   0.0007688999176025391 sec
    Recursive_v2:    0.0003693103790283203 sec
    Native pow:      4.6253204345703125e-05 s
"""