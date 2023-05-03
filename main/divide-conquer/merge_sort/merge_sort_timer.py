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
def quicksort(items, i=0, j=None):
    if j == None: 
        j = len(items) - 1

    if i > j: 
        return # Base case
    
    pivot = items[j]
    for k in range(i, j + 1):

        if items[k] < pivot:
            items[i], items[k] = items[k], items[i] # swap items
            i = i + 1 # move pointer

        if items[k] == pivot:
            items[i], items[k] = items[k], items[i] # move pivot
    
    quicksort(items, 0, i - 1) # sort left partition
    quicksort(items, i + 1, j) # sort right partition

@timer
def native_sort(items):
    return items.sort()


# Time
lst = random.sample(range(0, 300000), 300000)

start, end = 0, 0
merge_sort(lst); t1 = end - start

start, end = 0, 0
native_sort(lst); t2 = end - start

print("merge_sort() 300000 items:", t1, "s")
print("sort() 300000 items:", t2, "s")

"""
    merge_sort() 300000 items:  3.0545575618743896 s
    sort() 300000 items:        0.10179662704467773 s
"""