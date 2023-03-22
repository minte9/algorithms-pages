""" Sum numbers in array - Head tail technique

Recursive/
We add the head to the sum of tail array.
The trail in array is one element smaller than original.
We'll end up calling the recursive funtion on an emtpt array.

Important/
We are able to head number and sum(tail) in recursive case,
because the return value of sum() is a single number value.

Iterative/
The recursive function isn't necessary, because it never does 
any backtracking over the data.
"""

# Recursive
def rsum(numbers):
    if len(numbers) == 0: # base case
        return 0
    head = numbers[0]
    tail = numbers[1:]
    res  = head + rsum(tail)
    return res

# Iterative
def isum(numbers):
    res = 0
    for n in numbers:
        res += n
    return res
    
# Tests
assert rsum([1, 2, 3])  == 6
assert rsum([1, 2, 0])  == 3
assert isum([1, 2, 3]) == 6
assert isum([1, 2, 0]) == 3

# Overflow
numbers = range(100000)
print(isum(numbers)) # 4999950000

try:
    numbers = range(1000) # Look here
    rsum(numbers)
except RecursionError as e: # maximum recursion depth exceeded 
    print(e)