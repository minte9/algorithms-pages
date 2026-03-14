""" READING LISTS - O(1)
------------------------
Accessing an item by list index takes a constant time: 1 step.
The computer "jumps" directly to the memory address of that index (number).

It's like opening a book to a specific page using a bookmark.
Time complexity is O(1)
----------------------- 
"""

data = ["apples", "bananas", "oranges"]

index = 1
item = data[index]  # Reading takes 1 step -> O(1)

print("Found item=", item)  # bananas
print("Steps =", 1)  # 1