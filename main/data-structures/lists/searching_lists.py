# SEARCHING LISTS - O(n)
# ----------------------
# Linear search from a list takes maximum n steps.

# Concept:
#   Check each item one by one until you find the target (or reach the end).
#   In the worst case, you look at every element - N steps for N items.
#
# Real-life analogy:
#   Looking for "oranges" in a grocery receipt by reaching each line from top to bottom.
#
# When to use:
#   - The list is unsorted.
#   - Simplicity is preferred over performance.
#   - The list is small, so the overhead is negligible.
#
# Time complexity:
#   Worst case: O(N) | Best case: O(1) is the first item matched
# ---------------------------------------

fruits = ["apples", "bananas", "oranges"]

def search_value(items, value):
    for i in range(len(items)):
        if value == items[i]:
            return i  # Found, return index
    return -1

item = "oranges"
index = search_value(fruits, item)
print(f"Found {item} at index {index}, steps = {index + 1}")  # O(N)

item = "apples"
index = search_value(fruits, item)
print(f"Found {item} at index {index}, steps = {index + 1}")  # O(1)

# -----------------------------------
# Found oranges at index 2, steps = 3
# Found apples at index 0, steps = 1
