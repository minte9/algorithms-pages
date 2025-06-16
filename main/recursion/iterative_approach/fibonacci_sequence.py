""" In Fibonacci sequence every number is the sum of previous two numbers.
    0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Iterrative approach, a loop and two variables (a, b)
The program needs to keep track only of the latest two numbers.
    0 1 1     0 1 1 2       0 1 1 2 3     0 1 1 2 3 5       ... 
    a b a+b     a b a+b         a b a+b         a b a+b

The recursive algorithm is much slower than the iterative, it repeats same calculation.
For example, in fibonacci(5) the fibonacci(2) is called four times!
"""

def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(1, n):
        nextb = a + b
        a = b
        b = nextb
        # a, b = b, a + b # oneline
    return b

def fibonacci_recursive(n):
    if n <= 2: 
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Tests
assert fibonacci_iterative(1) == 1
assert fibonacci_iterative(3) == 2
assert fibonacci_iterative(4) == 3
assert fibonacci_iterative(5) == 5
assert fibonacci_recursive(6) == 8
assert fibonacci_recursive(7) == 13

#Output
print("The third Fibonnaci number is:", fibonacci_iterative(3))
print("The forth Fibonnaci number is:", fibonacci_iterative(4))
print("The fifth Fibonnaci number is:", fibonacci_iterative(5))

# Time
import time
print("\nThe recursive algorithm is much slower than the iterative.")
print("Processing ...")
t1 = time.time(); n1 = fibonacci_iterative(100)
t2 = time.time(); n2 = fibonacci_recursive(36)
print("Iterative: fibonacci(100)", time.time() - t1, 's') 
print("Recursive: fibonacci(36) ", time.time() - t2, 's') 

"""
    The third Fibonnaci number is: 2
    The forth Fibonnaci number is: 3
    The fifth Fibonnaci number is: 5

    The recursive algorithm is much slower than the iterative.
    Processing ...
    Iterative: fibonacci(100) 2.685002088546753 s
    Recursive: fibonacci(36)  2.6850242614746094 s
"""