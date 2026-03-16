""" BINARY SEARCH TREE (BST)
----------------------------
Tree: 
 - A tree is a data structure where each node can connect to other nodes
 - It is similar to how a family tree branches

BST Tree:
 - A binary tree is a tree where each node has up to TWO children.

Analogy:
 - Imagine a library shelf sorted alphabetically.
 - All books that start with letters BEFORE "M" go to the left.
 - All books that start with letters AFTER "M" go to the right.

This ordering helps searching very fast O(1).

Example: Sorting ages 
---------------------

     50
    /  \
   25  75

LEFT:  25 is younger (goes left)
RIGHT: 75 is older (goes right)
-------------------------------
"""

class Tree:
    # A node in the binary tree (optional left/right child nodes)
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right 

node1 = Tree(25)
node2 = Tree(75)
root = Tree(50, node1, node2)

# Checking the BST
assert root.value > root.left.value   # Left is smaller
assert root.value < root.right.value  # Right is larger

print("Tree ok")
