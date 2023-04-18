""" Sum numbers in array / Head tail technique

We add the head to the sum of tail array.
We are able to head number and sum(tail) in recursive case,
because the return value of sum() is a single number value.

The recursive function isn't necessary, because it never does 
any backtracking over the data. Also, it has a limit of 1000 calls.
"""

def head_tail_sum(numbers):
    if len(numbers) == 0: # Base case
        return 0
    head = numbers[0]
    tail = numbers[1:]
    res  = head + head_tail_sum(tail) # Recursive case
    return res

def sum(numbers):
    s = 0
    for n in numbers: 
        s += n
    return s
    
assert head_tail_sum([1, 2, 3])  == 6
assert head_tail_sum([1, 2, 0])  == 3
assert sum([1, 2, 3]) == 6
assert sum([1, 2, 0]) == 3

# Overflow
try:
    numbers = range(1000) # Look here
    head_tail_sum(numbers)
except RecursionError as e: # maximum recursion depth exceeded 
    print(e)

numbers = range(100000)
print(sum(numbers)) # 4999950000