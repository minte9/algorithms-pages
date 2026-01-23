# LINEAR SEARCH - O(n)
# --------------------
# Concept:
#   Check each element one by one until the target is found.
# 
# Why O(N)?
#   In the worst case, every element must be checked.
#   Steps grow directly with the number of elements.
# 
# Analogy: 
#   Looking for a name in an unsorted contact list
#   by scanning from top to bottom.
# 
# Best case: 
#   O(1) -> item is first
# 
# Worst case:
#   O(n) -> item is last or missing
# -------------------------------------------------

contacts = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']

def find_contact(contacts, name):
    steps = 0

    for i in range(len(contacts)):
        steps += 1

        if name == contacts[i]:  # found at index i
            return i, steps      # number of checkes: steps
            
    return -1, steps  # not found

index, steps = find_contact(contacts, 'Dave')

print(f"Found at index: {index} steps: {steps}")

# --------------------------
# Found at index: 3 steps: 4
