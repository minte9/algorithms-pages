# INSERTING SETS - O(1)
# ---------------------
# In terms of time compexity, the only difference 
# between arrays and sets is at insertion:
#   - Reading O(1)
#   - Searching O(N)
#   - Inserting O(1)
#   - Deleting O(N)
#
# Concept:
#   A set stores UNIQUE, UNORDERD elements. It rejects duplicates.
#   Insertion is (on average) O(1) thanks to hashing.
#
# Analogy:
#   Think of a guest list where each name can appear only once.
#   Adding a new name is instant; trying to add an existing name changes nothing.
#
# Time complexity: 
#   Average: O(1) to check + insert 
#
# Notes:
#   - Order is NOT guaranteed, SET chooses the storage location.
#   - Duplicates are ignored (no change to the set).
#   - This function MUTATES the input set.
# ---------------------------------------

fruits = {'apples', 'bananas', 'oranges'}

def add_item(items, value):
    steps = 0

    # Duplicate check
    for item in items:
        steps += 1
        if item == value:
            return -1

    # Not found -> insert
    items.add(value)

    steps += 1
    return steps

steps = add_item(fruits, 'kiwi')

print(fruits, steps) 

# ------------------------------
# {'bananas', 'apples', 'kiwi', 'oranges'} 4
