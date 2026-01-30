# BINERY SEARCH TREE - POPULATE
# ------------------------------
# Problem:
#   Insert data into BST (each node in the correct position)
#
# Example:
#   Input: [4, 2, 3, 1, 7, 6]  
#   Expected Output: [4 2 1 3 7 6]
#
# Goal:
#   Insert values into a BST so that:
#   - left subtree  < node
#   - right subtree > node
#
# Key idea:
#   - We WALK DOWN the tree using recursion
#   - We INSERT only when we find a None child
#   - We RETURN existing nodes to preserve the tree
# -------------------------------------------------

items = [4, 2, 3, 1, 7, 6]  

class Node:
    def __init__(self, val):
        self.info = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):

        # BOOTSTRAP CASE:
        # -------------------------------------------------------
        # If the tree is empty, the first value becomes the root.
        # No recursion needed here.
        # -------------------------------------------------------
        if self.root is None:
            self.root = Node(val)
        else:      
            # Otherwise, start walking the tree from the root                         
            self.populate(self.root, val)
    
    def populate(self, node, val):

        # MOVE DOWN: LEFT SUBTREE
        # -----------------------
        if val < node.info:

            # BASE CASE (ACTUAL INSERTION POINT)
            # -------------------------------------
            # We found an empty spot -> insert here
            # -------------------------------------
            if node.left is None:           
                node.left = Node(val)

            # RECURSIVE STEP: 
            # -------------------------------------
            # Left child exists -> keep walking down
            # ---------------------------------------
            else:
                node.left = self.populate(node.left, val)

        # MOVE DOWN: RIGHT SUBTREE
        # ------------------------
        if val > node.info:
            if node.right is None:          
                node.right = Node(val)      
            else:
                node.right = self.populate(node.right, val)

        return node
        

# BUILD THE TREE
# --------------
tree = BinarySearchTree()

for x in items:
    tree.insert(x)

# PREORDER TRAVERSAL OUTPUT
# -------------------------
def printTree(root):
    if root is None:
        return
    print(root.info, end=" ")
    printTree(root.left) 
    printTree(root.right) 

printTree(tree.root)  
# ------------------
# 4 2 1 3 7 6


# -------------------------------
# TESTING
# --------------------------------
def accumulate(root, output=None):  # No mutable default argument (recommended)
    if output is None:
        output = []

    if root is None:
        return
    
    output.append(root.info)        # Insert value
    accumulate(root.left, output)   # Recursion
    accumulate(root.right, output)  # Recursion

    return output

def populate(input):
    tree = BinarySearchTree()
    for x in input:
        tree.insert(x)
    return tree

# TEST / BALANCED INPUT
input = [4, 2, 3, 1, 7, 6]
tree = populate(input)
output = accumulate(tree.root)
assert  output == [4, 2, 1, 3, 7, 6]

# TEST / NEGATIVE VALUES
input = [0, -10, 10, -20, -5, 5, 20]
tree = populate(input)
output = accumulate(tree.root)
assert output == [0, -10, -20, -5, 10, 5, 20]

# TEST / DUPLICATES
input = [4, 2, 4, 2, 3]
tree = populate(input)
output = accumulate(tree.root)
assert output == [4, 2, 3]

# TEST / RANDOM INSERTION ORDER
input = [8, 3, 10, 1, 6, 14, 4, 7, 13]
tree = populate(input)
output = accumulate(tree.root)
assert output == [8, 3, 1, 6, 4, 7, 10, 14, 13]
                   
print("Tests passed")