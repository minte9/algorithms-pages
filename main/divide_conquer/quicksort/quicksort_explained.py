""" Quicksort - Recursive sorting algorithm
Developed by computer scientist Tony Hoare in 1959

Quicksort uses a divide-conquer technique called partitioning.
For example, we can have a large number of unordered books.
We can separate the books in two piles A-M and N-Z, so the 
the M would be the pivot.

If you keep partitioning you end up with piles that contain 
one book (the base case). And the piles are now sorted.
"""

def quicksort(items, i=0, j=None):
    
    if j == None: j = len(items) - 1

    if i > j: 
        return # stop sorting (base case)
    
    pivot = items[j]

    for k in range(i, j + 1):

        if items[k] < pivot:

            if i != k:
                print(items, f"Swap items", items[k], "with", items[i])
                items[i], items[k] = items[k], items[i] # swap items

            i = i + 1

        if items[k] == pivot:
            
            if i != k:
                print(items, "Move the pivot", pivot)
                items[i], items[k] = items[k], items[i] # move pivot
                print(items, "\n")
     
    print(items[0:i], pivot, items[i+1:j])

    quicksort(items, 0, i - 1) # sort left partition
    quicksort(items, i + 1, j) # sort right partition


data = [8, 18, 4, 2, 10]
print(data)

quicksort(data)
print("\nSorted:", data)

"""

[8, 18, 4, 2, 10]
[8, 18, 4, 2, 10] Swap items 4 with 18
[8, 4, 18, 2, 10] Swap items 2 with 18
[8, 4, 2, 18, 10] Move the pivot 10
[8, 4, 2, 10, 18] 

[8, 4, 2] 10 []
[8, 4, 2, 10, 18] Move the pivot 2
[2, 4, 8, 10, 18] 

[] 2 [4]
[2, 4] 8 []
[2] 4 []
[] 2 []
[2, 4, 8, 10] 18 []
[2, 4, 8] 10 []
[2, 4] 8 []
[2] 4 []
[] 2 []

Sorted: [2, 4, 8, 10, 18]

"""