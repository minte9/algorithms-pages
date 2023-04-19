""" Karatsuba multiplication / Speed tests
"""

import time

def product(x, y):
    product = 0
    for _ in range(x):
        product += y
    return product

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
        return TABLE[(x, y)] # Base case

    x = str(x)
    y = str(y)
    if len(x) < len(y): x = strpad(x, len(y) - len(x), 'left')
    if len(y) < len(x): y = strpad(y, len(x) - len(y), 'left')  

    m = HALF_TABLE[len(x)]
    a, b = int(x[:m]), int(x[m:])
    c, d = int(y[:m]), int(y[m:])

    k1 = karatsuba(a, c)
    k2 = karatsuba(b, d)
    k3 = karatsuba(a + b, c + d)
    k4 = k3 - k2 - k1       

    k1 = strpad(str(k1), (len(x) - m) + (len(x) - m), 'right')
    k4 = strpad(str(k4), (len(x) - m), 'right')

    return int(k1) + int(k4) + int(k2)  

x = 123_456_789
y = 123_456_789

start = time.time()
total = karatsuba(x, y)
print(f"karatsuba() time: {time.time() - start}s {total}")

start = time.time()
total = product(x, y)
print(f"product()   time: {time.time() - start}s {total}")

"""
karatsuba() time: 0.00012040138244628906s 15241578750190521
product()   time: 5.010555028915405s 15241578750190521
"""