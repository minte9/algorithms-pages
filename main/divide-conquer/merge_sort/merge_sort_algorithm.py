""" Merge sort algorithm
Developed by computer scientist John von Neumann in 1945

Each recusive call divides the unsorted list into halves, 
dowm into lists of zero of one lengths.
Then, as the recursive calls return, these smaller lists 
are merged toghether into sorted order.

[3, 2, 4, 1, 5]
  [3]   [2]
  [2, 3]
   [1]   [5]
   [1, 5]
  [4]   [1, 5]
  [1, 4, 5]
 [2, 3]   [1, 4, 5]
 [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

"""

def merge_sort(items):
    if len(items) <= 1: # Base case
        return items
        
    m = len(items) // 2
    L = merge_sort(items[:m]) # Recursive case
    R = merge_sort(items[m:]) # Recursive case

    i = 0
    j = 0
    sorted = []
    while len(sorted) < len(items):

        if L[i] < R[j]: # Append the smaller value 
            sorted.append(L[i])
            i = i + 1
        else:
            sorted.append(R[j])
            j = j + 1

        # end of each list
        if i == len(L): sorted.extend(R[j:])
        if j == len(R): sorted.extend(L[i:])
        
    return sorted

data = [3, 2, 4, 1, 5]
sorted = merge_sort(data)
print(data)     # [3, 2, 4, 1, 5]
print(sorted)   # [1, 2, 3, 4, 5]
