""" Quicksort / Recursive sorting algorithm

Developed by computer scientist Tony Hoare in 1959
It uses a divide-conquer technique called partitioning.

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
    j = len(items) - 1 if j == None else j

    if i > j: return # Base case

    pivot = items[j]
    for k in range(i, j + 1):
        if items[k] < pivot:
            items[i], items[k] = items[k], items[i] # swap items
            i = i + 1                               # move pointer
        if items[k] == pivot:
            items[i], items[k] = items[k], items[i] # move pivot
            
    quicksort(items, 0, i - 1) # left partition
    quicksort(items, i + 1, j) # right partition

data = [8, 18, 4, 2, 10]; 
print("Data:\t", data)  # [8, 18, 4, 2, 10]
quicksort(data); 
print("Sorted:\t", data) # [2, 4, 8, 10, 18]