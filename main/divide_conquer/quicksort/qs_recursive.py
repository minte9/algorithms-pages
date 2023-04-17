""" Quicksort - Recursive sorting algorithm

Developed by computer scientist Tony Hoare in 1959
It uses a divide-conquer technique called partitioning.

For example, we can have a large number of unordered books.
We can separate the books in two piles A-M and N-Z, so the 
the M would be the pivot.

If you keep partitioning you end up with piles that contain 
one book (the base case). And the piles are now sorted.
"""

def quicksort(items, i=0, j=None):
    
    if j == None: 
        j = len(items) - 1

    if i > j: 
        return # stop sorting (base case)

    pivot = items[j]

    for k in range(i, j + 1):
        if items[k] < pivot:
            items[i], items[k] = items[k], items[i] # swap items
            i = i + 1
        if items[k] == pivot:
            items[i], items[k] = items[k], items[i] # move pivot
            
    quicksort(items, 0, i - 1) # sort left partition
    quicksort(items, i + 1, j) # sort right partition

data = [8, 18, 4, 2, 10]
print("Data:\t", data) # [8, 18, 4, 2, 10]

quicksort(data)
print("Sorted:\t", data) # [2, 4, 8, 10, 18]