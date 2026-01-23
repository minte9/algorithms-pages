# INSERT LISTS - O(n)
# -------------------
# Inserting into a specific index in a list takes maximum n steps.

# Concept:
#   To insert at position key, we first make space by shifting all elements
#   from the right toward the end, then place the new value.
#
# Why N+1 steps?
#   - Up to N shifts (to move items and make space)
#   - +1 step to write teh new value into position
# 
# Real-life analogy:
#   In a row of theater seats, to seat a new person in the middle,
#   everyone to the right has to move over one seat.
#
# When to use:
#   When order matters and you must insert at a specific position.
#
# Time complexity:
#   O(N) - shifts grow with the number of elements to the right of key.
# ----------------------------------------

fruits = ["apples", "bananas", "oranges"]

def add(data, k, value):
    steps = 0

    # Create new list to avoid list being changed in place (lists are mutable)
    items = data[:]  

    # add one empty element at the end
    items.append("")
    
    # from end down to the k+1
    for i in range(len(items), k+1, -1):  # start, stop (required), step
        items[i-1] = items[i-2]           # shift elements one position to the right  
        steps += 1

    # place the new value in the gap
    items[k] = value
    steps += 1
    return items, steps

res, steps = add(fruits, 1, "kiwi")
print(res, steps)  

res, steps = add(fruits, 2, "kiwi")
print(res, steps)  

assert add(fruits, 1, "kiwi") == (['apples', 'kiwi', 'bananas', 'oranges'], 3)
assert add(fruits, 2, "lemons") == (['apples', 'bananas', 'lemons', 'oranges'], 2)

# -------------------------------------------
# ['apples', 'kiwi', 'bananas', 'oranges'], 3
# ['apples', 'bananas', 'kiwi', 'oranges'], 2
