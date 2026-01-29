# BINARY SEARCH TREE (BST) - RECURSIVE INSERT
# -------------------------------------------
# BST RULE (structure that never change):
#   - Left child < current node value
#   - Right child > current node value
#
# Question 1: Smallest input?
#   -> Node is none
# 
# Question 2: What happens then?
#   -> Create end RETURN a new node
# 
# Question 3: How does it get smaller?
#   -> We move done ONE level (left or right)
#
# Question 4: What stays the same?
#   -> The BST ordering rule: left < node < right
#
# Question 5: What does the function return?
#   -> A Tree node (the root of this subtree)
#   -> Every recursive call MUST return a value
# ---------------------------------------------

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(node, value, depth=0):

    # STEP 1: SMALLEST possible input -> node is None
    # STEP 2: Create and RETURN a new Tree node
    # --------------
    if node is None:
        return Tree(value)  # Base case
    
    # STEP 3: RECURSION
    # Decide whether to go LEFT or RIGHT
    # The problem gets smaller because we move to a subtree
    # --------------------
    if value < node.value:
        node.left = insert(node.left, value, depth + 1)   # Insert into the left subtree
    
    if value > node.value:
        node.right = insert(node.right, value, depth + 1)  # Insert into the right subtree

    # STEP 4: STRUCTURE STAYS THE SAME
    # STEP 5: RETURN VALUE
    # ---------
    return node

tree = insert(None, 50)
tree = insert(tree, 25)
tree = insert(tree, 33)
tree = insert(tree, 31)

def print_tree(node, depth=0):
    if node is None:
        return
    
    print_tree(node.right, depth + 1)
    print("  " * depth + str(node.value))
    print_tree(node.left, depth + 1)

print_tree(tree)

# The tree is printed sideways
# ----------------------------
# 50
#     33
#       31
#   25