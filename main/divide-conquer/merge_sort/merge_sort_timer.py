""" Merge sort algorithm / Speed tests
"""

import random
import time
start, end = 0, 0

def timer(func):
    def wrapper(*args, **kwargs):
        global start, end

        if start == 0: 
            start = time.time()

        result = func(*args, **kwargs)
        end = time.time()
        return result
        
    return wrapper

@timer
def merge_sort(items):
    if len(items) <= 1: # Base case
        return items
        
    m = len(items) // 2
    L = merge_sort(items[:m]) # Recursive
    R = merge_sort(items[m:])
    
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

@timer
def native_sort(items):
    return items.sort()


# Time
lst = random.sample(range(0, 300000), 300000)

start, end = 0, 0
sorted = merge_sort(lst)
t1 = end - start

start, end = 0, 0
native_sort(lst)
t2 = end - start

print("merge_sort() 300000 items:", t1, "s")
print("sort() 300000 items:", t2, "s")

"""
    merge_sort() 300000 items:  3.0545575618743896 s
    sort() 300000 items:        0.10179662704467773 s
"""