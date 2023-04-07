""" Quicksort
Recursive sorting algorithm developed by computer scientist
Tony Hoare in 1959

Quicksort uses a divide-concuer technique called partitioning.
For example, we can have a large number of unordered books.
We can separate the books in two piles A-M and N-Z, so the 
the M would be the pivot.

If you keep partitioning you end up with piles that contain 
one book (the base case). And the piles are now sorted.

Params: left and right indexes of the search range
Process: the range half in size for each recursive call
Base case: a range to sort that is empty or has one item
"""

def quicksort(items, left=0, right=None):
    if right == None: 
        right = len(items) - 1
    if left >= right: # Base case
        return
    
    i = left
    pivot = items[right]
    for j in range(left, right+1):
        if items[j] < pivot:
            items[i], items[j] = items[j], items[i] # Swap values
            i = i + 1
        if items[j] == pivot:
            items[i], items[right] = items[right], items[i] # Move pivot

    quicksort(items, left, i-1)     # Recursive case
    quicksort(items, i + 1, right)  # Recursive case

import random
data = random.sample(range(1, 100), 30); print(data)
quicksort(data); print(data)
print("Done!")

"""

[13, 99, 59, 75, 6, 40, 82, 79, 76, 81, 27, 80, 91, 69, 97, 89, 47, 61, 95, 32, 23, 54, 83, 36, 88, 58, 1, 29, 96, 44]
[1, 6, 13, 23, 27, 29, 32, 36, 40, 44, 47, 54, 58, 59, 61, 69, 75, 76, 79, 80, 81, 82, 83, 88, 89, 91, 95, 96, 97, 99]
Done!

"""


def quicksort_print(items, left=0, right=None):

    if right == None: 
        right = len(items) - 1

    if left >= right: # Base case
        return
    
    # START PARTITIONING
    i = left
    pivot = items[right]

    CYAN, ENDC = '\033[96m', '\033[0m'
    print(CYAN)
    print(items[left:right+1], "PARTITION", ENDC)
    print("Pivot =", pivot)

    for j in range(left, right+1):
        
        if items[j] < pivot:

            print(f"Swap i={i} j={j} ", items[j], "with", items[i], end="  ")
            items[i], items[j] = items[j], items[i] # Swap values
            i = i + 1
            print(items, "i =", i)

        if items[j] == pivot:
            items[i], items[right] = items[right], items[i] # Move pivot
            print("Move the pivot to the left on i=", i)
            print(items)
    # END PARTITIONING

    quicksort_print(items, left, i-1)     # Recursive case
    quicksort_print(items, i + 1, right)  # Recursive case


data = [0, 7, 6, 3, 1, 2, 5, 4]
quicksort_print(data)
print("Done!")

"""

[0, 7, 6, 3, 1, 2, 5, 4] PARTITION 
Pivot = 4
Swap i=0 j=0  0 with 0  [0, 7, 6, 3, 1, 2, 5, 4] i = 1
Swap i=1 j=3  3 with 7  [0, 3, 6, 7, 1, 2, 5, 4] i = 2
Swap i=2 j=4  1 with 6  [0, 3, 1, 7, 6, 2, 5, 4] i = 3
Swap i=3 j=5  2 with 7  [0, 3, 1, 2, 6, 7, 5, 4] i = 4
Move the pivot to the left on i= 4
[0, 3, 1, 2, 4, 7, 5, 6]

[0, 3, 1, 2] PARTITION 
Pivot = 2
Swap i=0 j=0  0 with 0  [0, 3, 1, 2, 4, 7, 5, 6] i = 1
Swap i=1 j=2  1 with 3  [0, 1, 3, 2, 4, 7, 5, 6] i = 2
Move the pivot to the left on i= 2
[0, 1, 2, 3, 4, 7, 5, 6]

[0, 1] PARTITION 
Pivot = 1
Swap i=0 j=0  0 with 0  [0, 1, 2, 3, 4, 7, 5, 6] i = 1
Move the pivot to the left on i= 1
[0, 1, 2, 3, 4, 7, 5, 6]

[7, 5, 6] PARTITION 
Pivot = 6
Swap i=5 j=6  5 with 7  [0, 1, 2, 3, 4, 5, 7, 6] i = 6
Move the pivot to the left on i= 6
[0, 1, 2, 3, 4, 5, 6, 7]
Done!

"""