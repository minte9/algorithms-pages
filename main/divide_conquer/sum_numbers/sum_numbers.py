""" Sum numbers / Divide and conquer technique

Addition is associative, 1+2+3+4 is the same as 1+2 and 3+4
We can divide a large array of numbers into smaller arrays to sum.

This a large advantage of this technique, because CPU aren't getting 
much faster, but we can have multiple CPUs running in paralel.
"""

def sumDC(numbers):
    if len(numbers) == 0: return 0          # Base case
    if len(numbers) == 1: return numbers[0] # Base case

    m = len(numbers) // 2
    left  = sumDC(numbers[:m]) # Recursive case
    right = sumDC(numbers[m:]) # Recursive case

    return left + right

assert sumDC([1, 2, 3, 4, 5]) == 15
assert sumDC([5, 2, 4, 8]) == 19
assert sumDC([1, 10, 100, 1000]) == 1111