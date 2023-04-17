""" Merge sort
"""

def merge_sort(items):

    if len(items) <= 1: # Base case
        return items

    middle = len(items) // 2

    left  = merge_sort(items[:middle])
    right = merge_sort(items[middle:])

    print(left, "\t", right)
    # At this stage left and right are sorted (1 item)

    sorted = []
    i = 0
    j = 0
    while len(sorted) < len(items):

        # Append the smaller value
        if left[i] < right[j]:
            sorted.append(left[i])
            i = i + 1
        else:
            sorted.append(right[j])
            j = j + 1

        # If one of the pointers has reached the end of its list,
        # put the rest of the other list into sorted list
        if i == len(left):
            sorted.extend(right[j:])
            break
        if j == len(right):
            sorted.extend(left[i:])
            break

    return sorted

data = [2, 9, 8, 5, 3, 4, 7, 6]
sorted = merge_sort(data)
print(data)
print(sorted)