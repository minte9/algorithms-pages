""" Quicksort / Algorithm runtime
Around 480 items maximum
"""

import random
import time

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


# Quicksort on 100 items
list = random.sample(range(0, 100), 100)
start = time.time()
quicksort(list)
t1 = time.time() - start

# Quicksort on 480 items (aprox. stack overflow limit)
list = random.sample(range(0, 480), 480)
start = time.time()
quicksort(list)
t2 = time.time() - start

# Python built-in sort
list = random.sample(range(0, 300000), 300000)
start = time.time()
list.sort()
t3 = time.time() - start

# Output times
print("quicksort() 100 items:", t1, "s")
print("quicksort() 480 items:", t2, "s")
print("sort() 300000 items:", t3, "s")

"""
    quicksort() 100 items: 0.01451730728149414 s
    quicksort() 480 items: 1.3930106163024902 s
    sort() 300000 items:   0.06310772895812988 s
"""