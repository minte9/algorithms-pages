""" BST SEARCH
--------------
Recursion:
 - Tree have levels inside levels
 - Recursion lets a function call itself
 - It goes down the correct branch until it finds a match

How BST search works:
 - If target == node.value -> found it (base case)
 - If target < node.value -> go LEFT (smaller values)
 - If target > node.value -> go RIGHT (larger values)

Edge cases:
 - If we reach a None node, the value is not in the tree
 - If empty tree return None immediately

Build a sample BST:
-------------------------------
               50
           /         \
         25           75
       /    \       /     \
     10     33    56       89
    /  \   /  \  /  \     /  \
   4   11 30  40 52 61   82  95

-------------------------------
"""

class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def search(value, node):
    # Base case: tree or branch ended without a match
    if node is None:
        return None

    # Base case: found the value at the current node
    if value == node.value:
        return node

    # Recursive cases: pick a side (left, right)
    if value < node.value:
        return search(value, node.left)

    if value > node.value:
        return search(value, node.right)

# Level 2
node7 = Tree(89, Tree(82), Tree(95))
node6 = Tree(56, Tree(52), Tree(61))
node5 = Tree(33, Tree(30), Tree(40))
node4 = Tree(10, Tree(4), Tree(11))

# Level 1
node3 = Tree(75, node6, node7)
node2 = Tree(25, node4, node5)

# Level 0 (root)
node1 = Tree(50, node2, node3)

# Example searches
node = search(61, node1)
print(node.value if node else None)  # 61

node = search(13, node1)  # 13 is not in the tree
print(node)               # None