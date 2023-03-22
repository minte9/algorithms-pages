""" Fibonacci sequence
Every number is the sum of previous two numbers

1 1 2       1 1 2 3     1 1 2 3 5       ...
a b a+b       a b a+b       a b a+b

Iterrative approach, a loop and two variables (a, b)
The program needs to keep track only of the latest two numbers.

The recursive algorithm is much slower than the iterative one.
It repeats same calculation over and over.
For fibonacci(5) the fibonacci(2) is called four times!
"""

# Iterative
def ifibonacci(n):
    a, b = 1, 1
    for i in range(1, n-1):
        nextb = a + b
        a = b
        b = nextb
        # a, b = b, a + b # oneline
    return b

# Recursive
def rfibonacci(n):
    if n == 1: return 1
    if n == 2: return 1
    return rfibonacci(n-1) + rfibonacci(n-2)

# Tests
assert ifibonacci(2) == 1
assert ifibonacci(3) == 2
assert ifibonacci(4) == 3
assert ifibonacci(5) == 5
assert rfibonacci(6) == 8
assert rfibonacci(7) == 13

# Limits
import time
start = time.time(); n = rfibonacci(36); end = time.time()
print(n, end-start, 'seconds') 
    # 14930352 / 2.6 seconds
    
start = time.time(); n = ifibonacci(100); end = time.time()
print(n, end-start, 'seconds') 
    # 354224848179261915075 / 0.000009 seconds