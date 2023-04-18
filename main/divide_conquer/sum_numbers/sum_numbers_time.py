""" Sum numbers / Divide and conquer technique

Addition is associative, 1+2+3+4 is the same as 1+2 and 3+4
We can divide a large array of numbers into smaller arrays to sum.

This a large advantage of this technique, because CPU aren't getting 
much faster, but we can have multiple CPUs running in paralel.
"""

import time
import random

def sumDC(numbers):
    if len(numbers) == 0: return 0          # Base case
    if len(numbers) == 1: return numbers[0] # Base case

    m = len(numbers) // 2
    left  = sumDC(numbers[:m]) # Recursive case
    right = sumDC(numbers[m:]) # Recursive case
    return left + right

n = 1000000
data = random.sample(range(0, n), n)
start = time.time()
total = sumDC(data)
print(f"{n} sumDC()  time: {time.time()  - start} s \t {total}")

start = time.time()
total = sum(data)
print(f"{n} sum() \t time: {time.time() - start} s \t {total}")

"""
1000000 sumDC()  time: 0.7261147499084473 s      499999500000
1000000 sum()    time: 0.03888964653015137 s     499999500000
"""