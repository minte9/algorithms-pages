""" Factorial 4! = 4x3x2x1
Many computer science courses use factorial calculation 
as a classic example of a recursive function.
Factorials are use for example in finding permutations number.
    
Iterrative approch, multiplies intergers 1 to n in a loop
Recursive approach, uses neighbours 5! = 5 * 4!

The recursive implementation requires 5 frame objects
The iterrative implementation, only 1.
"""

def ifactorial(n): # Iterrative
    p = 1
    for i in range(1, n+1):
        p = p * i
    return p

def rfactorial(n): # Recursive 
    if n == 1:
        return 1
    return n * rfactorial(n-1)

# Tests
assert ifactorial(4) == 24
assert ifactorial(5) == 120
assert rfactorial(5) == 5 * rfactorial(4)
assert rfactorial(4) == 4 * rfactorial(3)

# Limits
n = ifactorial(1001)
print(len(str(n))) # 2571
try:    
    n = rfactorial(1001)
except RecursionError as e:
    print(e) # maximum recursion depth exceeded in comparison