""" Quicksort / Algorithm runtime
Around 480 items maximum
"""

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
import random
import time
start, end = 0, 0

lst = random.sample(range(0, 100), 100)
start, end = 0, 0
quicksort(lst)
t1 = end - start

lst = random.sample(range(0, 480), 480) # stack overlow limit
start, end = 0, 0
quicksort(lst)
t2 = end - start

lst = random.sample(range(0, 300000), 300000)
start, end = 0, 0
native_sort(lst)
t3 = end - start

print("quicksort() 100 items:", t1, "s")
print("quicksort() 480 items:", t2, "s")
print("sort() 300000 items:", t3, "s")

"""
    quicksort() 100 items: 0.01451730728149414 s
    quicksort() 480 items: 1.3930106163024902 s
    sort() 300000 items:   0.06310772895812988 s
"""