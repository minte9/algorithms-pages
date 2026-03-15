""" LINEAR SEARCH - O(n)
------------------------
Check each element one by one until the target is found.

It's like looking for a name in an unsorted contact list
by scanning from top to bottom.

Time Complexity O(n):
O(1) - searched item is first (best case)
O(n) - searched item is last or missing (worst case)
----------------------------------------------------
"""

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
