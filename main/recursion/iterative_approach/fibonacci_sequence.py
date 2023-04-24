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

def fibonacci(n): # Iterative
    a, b = 1, 1
    for i in range(1, n-1):
        nextb = a + b
        a = b
        b = nextb
        # a, b = b, a + b # oneline
    return b

def fibonacci_recursive(n):
    if n == 1: return 1
    if n == 2: return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Tests
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci_recursive(6) == 8
assert fibonacci_recursive(7) == 13

# Limits
import time
start = time.time(); n = fibonacci(100); end = time.time()
print("Iterative: fibonacci(100) =", n, end-start, 'seconds') 

start = time.time(); n = fibonacci_recursive(36); end = time.time()
print("Recursive: fibonacci(36)  =", n, "\t\t", end-start, 'seconds') 

# Iterative: fibonacci(100) = 354224848179261915075 7.152557373046875e-06 seconds
# Recursive: fibonacci(36)  = 14930352             2.724464178085327 seconds