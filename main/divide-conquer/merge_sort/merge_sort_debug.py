""" Merge sort / Algorithm Debug
"""

def merge_sort(items, depth=0):

    if len(items) <= 1: # Base case
        return items

    m = len(items) // 2
    L = merge_sort(items[:m], depth + 1) # Recursive case
    R = merge_sort(items[m:], depth + 1) # Recursive case
    
    # At this stage left and right are sorted
    print(depth * " ", L, " ", R) 

    i = 0
    j = 0
    sorted = []
    while len(sorted) < len(items):

        # Append the smaller value and advance to next item
        if L[i] < R[j]:
            sorted.append(L[i])
            i = i + 1
        else:
            sorted.append(R[j])
            j = j + 1

        # If one of the pointers has reached the end of its list,
        # put the rest of the other list into sorted list
        if i == len(L):
            sorted.extend(R[j:])
            break
        if j == len(R):
            sorted.extend(L[i:])
            break
    
    print(depth * " ", sorted) 
    return sorted

data = [2, 9, 8, 5, 3, 4, 7, 6]
print(data)

sorted = merge_sort(data)
print(sorted)

"""

[2, 9, 8, 5, 3, 4, 7, 6]
   [2]   [9]
   [2, 9]
   [8]   [5]
   [5, 8]
  [2, 9]   [5, 8]
  [2, 5, 8, 9]
   [3]   [4]
   [3, 4]
   [7]   [6]
   [6, 7]
  [3, 4]   [6, 7]
  [3, 4, 6, 7]
 [2, 5, 8, 9]   [3, 4, 6, 7]
 [2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7, 8, 9]

"""