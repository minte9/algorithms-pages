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

def fibonacci_iterative(n):
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

assert fibonacci_iterative(2) == 1
assert fibonacci_iterative(3) == 2
assert fibonacci_iterative(4) == 3
assert fibonacci_iterative(5) == 5
assert fibonacci_recursive(6) == 8
assert fibonacci_recursive(7) == 13

import time
t1 = time.time(); n1 = fibonacci_iterative(100)
t2 = time.time(); n2 = fibonacci_recursive(36)
print("Iterative: fibonacci(100)", time.time() - t1, 's') 
print("Recursive: fibonacci(36) ", time.time() - t2, 's') 

"""
    Iterative: fibonacci(100) 2.5802948474884033 s
    Recursive: fibonacci(36)  2.5803282260894775 s
"""