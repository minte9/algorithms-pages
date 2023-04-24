""" Factorial 4! = 4x3x2x1
Factorials are use for example in finding permutations number.

Recursive, uses neighbours 5! = 5 * 4!
5 frame objects

Iterrative, multiplies intergers 1 to n in a loop, 
1 frame object, better!

"""

def factorial(n): # Iterative
    p = 1
    for i in range(1, n+1):
        p = p * i
    return p

def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)

# Tests
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial_recursive(5) == 5 * factorial_recursive(4)
assert factorial_recursive(4) == 4 * factorial_recursive(3)

# Limits
n = factorial(1001)
print(len(str(n))) # 2571
try:    
    n = factorial_recursive(1001)
except RecursionError as e:
    print(e) # maximum recursion depth exceeded in comparison