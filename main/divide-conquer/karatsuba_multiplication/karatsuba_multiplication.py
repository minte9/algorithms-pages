""" Karatsuba Multiplication Algorithm

Fast multiplication algorithm, developed by Anatoly Karatsuba 
in 1960, at the age of 23!

The * operator makes multiplication easy in high-level languages.
But low-level hardware need a way that uses more primitive operations.

We could implement it using a loop, but it is slow. 
Karatsuba used a precomputed table of products for single digits numbers.

1357 x 2467
    = (10^2*13 + 57) * (10^2*24 + 67) 
ab x cd
    = (10^(n/2)*a + b) * (10^(n/2)*c + d)
    = 10^n*ac + 10^(n/2)*(ad + bc) + bd
    = 10^n*k1 + 10^(n/2)*k4 + k2
"""

# Normaly, lookup tables are hardcoded in the code
TABLE = {}
for i in range(10):
    for j in range(10):
        TABLE[(i, j)] = i * j

HALF_TABLE = []
for i in range(100):
    HALF_TABLE.append(i // 2)

def strpad(str, n, padding='left', chr='0'):
    if padding == 'left':
        return n * chr + str
    return str + n * chr

def karatsuba(x, y):
    assert isinstance(x, int), 'x must be integer'
    assert isinstance(y, int), 'y must be integer'
    if x < 10 and y < 10: 
        return TABLE[(x, y)] # Base case (single digits numbers)

    # Pad with zeros (so x and y will have same length)
    x = str(x)
    y = str(y)
    if len(x) < len(y): x = strpad(x, len(y) - len(x), 'left')
    if len(y) < len(x): y = strpad(y, len(x) - len(y), 'left')  

    # Split x and y into halves
    m = HALF_TABLE[len(x)]
    a, b = int(x[:m]), int(x[m:])
    c, d = int(y[:m]), int(y[m:])

    # Recusive calls
    k1 = karatsuba(a, c)            # ac
    k2 = karatsuba(b, d)            # bd
    k3 = karatsuba(a + b, c + d)    # ac + ad + bc + bd
    k4 = k3 - k2 - k1               # ad + bc

    # Add zeros (as multiply with 10s)
    k1 = strpad(str(k1), (len(x) - m) + (len(x) - m), 'right')  # 10^n*k1 
    k4 = strpad(str(k4), (len(x) - m), 'right')                 # 10^(n/2)*k4

    return int(k1) + int(k4) + int(k2)  

def linear_product(x, y):
    product = 0
    for _ in range(x):
        product += y
    return product

def native_product(x, y):
    return x * y

# Tests
assert karatsuba(10, 20) == 200
assert karatsuba(90, 900) == 81000
assert karatsuba(1357, 2468) == 3349076

# Time
import time
x = 123_456_789
y = 123_456_789

t0 = time.time()
p1 = karatsuba(x, y); t1 = time.time() - t0

t0 = time.time()
p2 = linear_product(x, y); t2 = time.time() - t0

t0 = time.time()
p3 = native_product(x, y); t3 = time.time() - t0

assert p1 == p2
print("karatsuba()", t1, "s")
print("linear_product()", t2, "s")
print("native_product()", t3, "s")

"""
    karatsuba()      0.0003743171691894531 s
    linear_product() 8.377368927001953 s
    native_product() 3.0994415283203125e-06 s
"""