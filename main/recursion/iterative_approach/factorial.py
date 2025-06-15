""" A factorial, denoted by an exclamation point (n!), is the product of 
all positive integers less than or equal to a given non-negative integer n 
4! = 4x3x2x1

Iterrative, multiplies intergers 1 to n in a loop, 
1 frame object (function call)

Recursive, uses neighbours 5! = 5 * 4!
5 frame objects 
"""

def factorial_iterative(n):
    p = 1
    for i in range(1, n+1):
        p = p * i
    return p

def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)

assert factorial_iterative(4) == 24
assert factorial_recursive(5) == 5 * factorial_recursive(4)

# Limits
n = factorial_iterative(30000)
print(f"Iterative factorial 30.000 iterations:", len(str(n)))

# Recursive approach limit (< 3000)
try:    
    n = factorial_recursive(3000)
except RecursionError as e:
    print(f"Recursive factorial 3.000 iterations limit reached!")
    print(f"RecursionError: {e}")

"""
    Iterative factorial 30.000 iterations: 121288
    Recursive factorial 3.000 iterations limit reached!
    RecursionError: maximum recursion depth exceeded in comparison
"""