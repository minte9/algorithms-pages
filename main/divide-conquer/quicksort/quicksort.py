""" Quicksort / Recursive sorting algorithm
Uses a divide-conquer technique called partitioning.

For example, we can have a large number of unordered books.
We can separate the books in two piles A-M and N-Z, so the 
the M would be the pivot. 

Usually at start the item on the right is choosed as pivot.
We compare the left item with the pivot.
If left < right, we swap the items, and then move the left pointer with +1 

When we rich the pivot, we automatically swap the items, 
then call the recursion on the two new partitions.

2, 12, 9, 7, 8      / pivot=8, i=0, k=0
2< 8                / swap 2 with itself, i+1
2, 12, 9, 7, 8      / pivot=8, i=1, k=1
          7< 8      / swap 7 with 12, i+1
1, 7, 9, 12, 8      / pivot=8, i=2, k=3
             8=8    / swap pivot with 9
1, 7, 8, 12, 9    

1, 7                / left partition
12, 9               / right partition
continue ...

"""

def quicksort(items, i=0, j=None):
    if j == None: 
        j = len(items) - 1

    if i > j: 
        return # Base case
    
    pivot = items[j]
    for k in range(i, j + 1):

        if items[k] < pivot:
            if i != k:
                print(items, f"Swap items", items[k], "with", items[i])
                items[i], items[k] = items[k], items[i] # swap items
            i = i + 1 # move pointer

        if items[k] == pivot:
            if i != k:
                print(items, "Move the pivot", pivot)
                items[i], items[k] = items[k], items[i] # move pivot
                print(items, "\n")
     
    print(items[0:i], pivot, items[i+1:j])
    quicksort(items, 0, i - 1) # sort left partition
    quicksort(items, i + 1, j) # sort right partition


data = [8, 18, 4, 2, 10]; 
print("Data:", data)  # [8, 18, 4, 2, 10]

quicksort(data); 
print("Sorted:", data) # [2, 4, 8, 10, 18]

"""
    Data: [8, 18, 4, 2, 10]
    Sorted: [2, 4, 8, 10, 18] 

    Data: [8, 18, 4, 2, 10]
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