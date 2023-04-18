""" Quicksort algorithm - Speed tests
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
def quicksort(items, i=0, j=None):
    if j == None: j = len(items) - 1
    if i > j: return # Base case
    
    pivot = items[j]
    for k in range(i, j + 1):
        if items[k] < pivot:
            items[i], items[k] = items[k], items[i] # swap items
            i = i + 1
        if items[k] == pivot:
            items[i], items[k] = items[k], items[i] # move pivot
    
    quicksort(items, 0, i - 1) # sort left partition
    quicksort(items, i + 1, j) # sort right partition

@timer_decorator
def native_sort(items):
    return items.sort()


""" Test speed with 100 items
"""
data = random.sample(range(0, 100), 100)
quicksort(data)
print("quicksort() 100  time:", end_time - start_time, "s")
start_time, end_time = None, None


""" Test speed with 480 items
A number larger than 480 will give error: maximum recursion depth error
"""
data = random.sample(range(0, 480), 480)
quicksort(data)
print("quicksort() 480  time:", end_time - start_time, "s")
start_time, end_time = None, None


""" Test with Python native sort() function
"""
data = random.sample(range(0, 300000), 300000)
native_sort(data)
print("sort() 300000 \t time:", end_time - start_time, "s")
start_time, end_time = None, None


"""

quicksort() 100  time: 0.01843881607055664 s
quicksort() 480  time: 1.216728687286377 s
sort() 300000    time: 0.0657494068145752 s

"""