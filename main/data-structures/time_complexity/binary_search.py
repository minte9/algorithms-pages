# BINARY SEARCH - O(log N)
# ------------------------
# Binary search is effective only on SORTED lists.
#
# Concept:
#   Reapeatedly split the search in half and discard the half 
#   that cannot contain the target.
# 
# Why O(log n)?
#   Each step cuts the search space in half. 
#   Doubling the data only adds ONE extra step.
#
# Compare the middle element to the target:
#   - If equal, we're done.
#   - If target is greater, search the right half.
#   - If smaller, search the left half.
# 
# Analogy:
#   Finding a word in a dictionary by jumping to the middle, 
#   and narrowing the seaction each time.
#
# Requirement:
#   The array MUST be sorted.
# 
# When to use:
#   - You need fast lookups (much faster than linear search for large N).
#
# Time complexity:
#   O(log N) comparisons in the worst case.
# -----------------------------------

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(items, val):
    left = 0
    right = len(items) - 1
    steps = 0

    while left <= right:
        steps += 1
        middle = (left + right) // 2

        if val == items[middle]:
            return middle, steps  # found

        if val > items[middle]:
            left = middle + 1
        else:
            right = middle -1

    return -1, steps  # not found


# 1) Small ordered list
# ---------------------
key, steps = binary_search(data, 7)
print(steps, key) # 4, 6


# 2) Doubling the list, the search increase with only 1 step
# ----------------------------------------------------------
data = [i for i in range(21)]
key, steps = binary_search(data, 17)
print(steps, key)  # 5, 17


# 3) For large sized list, the search is very fast
# ------------------------------------------------
data = list(range(100000))
key, steps = binary_search(data, 70000)
print(steps, key)  # 17, 70000
