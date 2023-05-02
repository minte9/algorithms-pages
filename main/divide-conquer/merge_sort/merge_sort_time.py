""" Merge sort algorithm / Speed tests
"""

import time
import random
start_time, end_time = None, None

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        global start_time, end_time
        if start_time is None: 
            start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result
    return wrapper

@timer_decorator
def merge_sort(items):
    if len(items) <= 1: # Base case
        return items
        
    m = len(items) // 2
    L = merge_sort(items[:m]) # Recursive case
    R = merge_sort(items[m:]) # Recursive case
    
    i = 0
    j = 0
    sorted = []
    while len(sorted) < len(items):

        if L[i] < R[j]:
            sorted.append(L[i])
            i = i + 1
        else:
            sorted.append(R[j])
            j = j + 1

        if i == len(L): sorted.extend(R[j:])
        if j == len(R): sorted.extend(L[i:])
    return sorted

@timer_decorator
def native_sort(items):
    return items.sort()


# merge_sort() time elapsed
data = random.sample(range(0, 300000), 300000)
sorted = merge_sort(data)
print("merge_sort()  300000 \t time:", end_time - start_time, "s")

# sort() time elapsed
start_time, end_time = None, None
native_sort(data)
print("native_sort() 300000 \t time:", end_time - start_time, "s")

# merge_sort()  300000     time: 1.7765398025512695 s
# native_sort() 300000     time: 0.07159161567687988 s
