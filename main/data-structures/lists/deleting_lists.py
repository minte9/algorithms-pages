# DELETING LISTS - O(n)
# ---------------------
# Deleteing from a list at a specific index takes maximum n steps.
#
# Concept:
#   To remove the item at key, we shift everything to its right one step left
#   to cover the gap, then remove the non-duplicate last element.
#
# Why N+1 steps?
#   - Up to N-1 shifts (elements to the right of the {{key`)
#   - +1 step to pop() the trailing duplicate
#
# Real-life analogy:
#   Pull a book from the middle of a tight shelf: every book to the right
#   slides left by one position to close the gap, then you tidy the end.
#
# Time complexity:
#   O(N) - proportional to how many elements are to the right of {{key`
#
# Note:
#   This function MUTATES the input list.
# ---------------------------------------

fruits = ["apples", "bananas", "oranges"]

def delete_item(data, k):
    steps = 0

    for i in range(k, len(data)-1):  # start at specific index
        data[i] = data[i+1]
        steps += 1

    data.pop()  # remove the duplicate last element
    steps += 1
    return steps

delete_item(fruits, 1)

print(fruits)

# -----------------------
  # ['apples', 'oranges']
