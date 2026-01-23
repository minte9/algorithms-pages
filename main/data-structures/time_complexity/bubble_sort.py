# BUBBLE SORT - O(n^2)
# --------------------
# Concept:
#   Swap adjiacent elements (repeatedly) if they are not sorted.
# 
# Why O(n^2)?
#   - One loop scans the list
#   - Another loop repeats the scan many times
#   -> Nested loops = quadratic growth
# 
# Analogy:
#   Sorting cards by repeatedly comparing neighbors,
#   over and over, until everything is in order.
# 
# Base case:
#   O(n) - already sorted, with optimization (keep track of right)
# 
# Worst case:
#   O(n^2) - reverse order 
# ------------------------------------

def bubble_sort(items):
    sorted = False
    steps = 0

    while not sorted:
        sorted = True

        for i in range(len(items)-1):
            steps += 1

            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i] # swap 
                sorted = False
                steps +=1

    return items, steps


data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
data, steps = bubble_sort(data)
print(data, steps)  
# -----------------------------------
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 135


# Bubble sort (optimized)
# -----------------------
def bubble_sort_optimized(items):
    sorted = False
    steps = 0
    right = len(items) - 1  # Look Here

    while not sorted:
        sorted = True
        for i in range(right):
            steps += 1
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i] # swap 
                steps +=1
                sorted = False

        right -= 1  # Look Here

    return items, steps

data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
data, steps = bubble_sort_optimized(data)
print(data, steps)  
# ----------------------------------
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 90


# Side‑by‑side comparison, explaining why O(n^2)
# ---------------------------------------------
print("n BS-steps n^2")

for n in [5, 10, 20, 40, 80]:
    arr = list(range(n, 0, -1))

    _, steps = bubble_sort_optimized(arr)
    print(n, steps, n**2)

# --------------
# n BS-steps n^2
# 5 20 25
# 10 90 100
# 20 380 400
# 40 1560 1600
# 80 6320 6400

