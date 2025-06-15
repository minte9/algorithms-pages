""" Exponents are calculated by multiplying a number by itself.
    res = x^n

Iterative approach uses a loop that repeatedly multiplies a number by itself:
    res = res * x

Recursive approach uses the power rule: 
    a^n = a^(n-1) * a^1 
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

assert pow_interative(2, 2) == 4
assert pow_recursive(3, 3) == 27
print("2^2 =", pow_interative(2,2))
print("3^3 =", pow_recursive(3,3))

# Time
import time
t1 = time.time(); result = pow_interative(3, 600)
t2 = time.time(); result = pow_recursive(3, 600)
t4 = time.time(); result = pow(3, 600)

print("Iterative  3^600: ", time.time() - t1, 's') 
print("Recursive  3^600: ", time.time() - t2, 'sec') 
print("Native pow 3^600: ", time.time() - t4, 's') 

"""
    2^2 = 4
    3^3 = 27
    Iterative  3^600:   0.0007915496826171875 s
    Recursive  3^600:   0.0007688999176025391 sec
    Native pow 3^600:      4.6253204345703125e-05 s
"""