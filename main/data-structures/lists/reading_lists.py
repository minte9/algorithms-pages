# READING LISTS - O(n)
# --------------------
# Reading from a list takes exactly 1 step.

# Concept:
#   Accessing an item by index in list takes a constant time: 1 step.
#   The computer "jumps" directly to the memory address of that index (number).
#
# Real-life analogy:
#   Like opening a book to a specific page using a bookmark.
#
# When to use:
#   Anytime you know the exact position (index) of the item you want.
#
# Time complexity:
#   O(1) - Constant time.
# ------------------------------------

data = ["apples", "bananas", "oranges"]

index = 1
item = data[index]  # Reading takes 1 step -> O(1)

print("Found item=", item)
print("Steps =", 1)

# --------------------
# Found item = bananas
# Steps = 1