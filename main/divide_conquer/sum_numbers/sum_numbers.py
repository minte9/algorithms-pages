""" Sum numbers

-- Divide and conquer technique
Addition is associative, 1+2+3+4 is the same as 1+2 and 3+4
We can divide a large array of numbers into smaller arrays to sum.
This a large advantage of this technique, because CPU aren't getting 
much faster, but we can have multiple CPUs running in paralel.

-- Head tail technique
We add the head to the sum of tail array.
We are able to head number and sum(tail) in recursive case,
because the return value of sum() is a single number value.

-- Iterative
The recursive function isn't necessary, because it never does 
any backtracking over the data. Also, it has a limit of 1000 calls.

"""

def sum_numbers_divide_conquer(numbers):
    if len(numbers) == 0: return 0          # Base cases
    if len(numbers) == 1: return numbers[0]

    m = len(numbers) // 2
    left  = sum_numbers_divide_conquer(numbers[:m]) # Recursive
    right = sum_numbers_divide_conquer(numbers[m:])

    return left + right

def sum_numbers_head_tail(numbers):
    if len(numbers) == 0: # Base case
        return 0

    head = numbers[0]
    tail = numbers[1:]
    res  = head + sum_numbers_head_tail(tail) # Recursive
    return res

def sum_numbers_iterative(numbers):
    s = 0
    for n in numbers: 
        s += n
    return s

def native_sum(numbers):
    return sum(numbers)


# Tests
assert sum_numbers_divide_conquer([1, 2, 3, 4, 5]) == 15
assert sum_numbers_divide_conquer([5, 2, 4, 8]) == 19
assert sum_numbers_divide_conquer([1, 10, 100, 1000]) == 1111

assert sum_numbers_head_tail([1, 2, 3])  == 6
assert sum_numbers_head_tail([1, 2, 0])  == 3

assert sum_numbers_iterative([1, 2, 3]) == 6
assert sum_numbers_iterative([1, 2, 0]) == 3


# Speed
import time, random
n = 1000000

# Divide conquer
data = random.sample(range(0, n), n)
start = time.time()
total = sum_numbers_divide_conquer(data)
print(f"divide_conquer() time: {time.time()  - start} s")

# Head tail
try:   
    sum_numbers_head_tail(range(1000))
except RecursionError as e: 
    print("head_tail() 1000:", e) # maximum recursion depth exceeded (Overflow)

# Native sum
start = time.time()
total = sum(data)
print(f"native_sum() time: {time.time() - start} s")

# Iterative
start = time.time()
total = sum_numbers_iterative(data)
print(f"iterative() time: {time.time() - start} s")

"""

divide_conquer() time:  0.8668022155761719 s
head_tail()             1000: maximum recursion depth exceeded ...
native_sum() time:      0.04935026168823242 s
iterative() time:       0.16187739372253418 s

"""