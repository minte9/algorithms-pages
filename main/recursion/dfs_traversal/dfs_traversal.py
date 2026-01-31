# DFS - Depth-First Search TRAVERSAL
# ----------------------------------
# Concept:
#   - Depth-First Search explores a tree by going as deep
#     as possible along each branch before backtracking.
# 
# Variants:
#   - For Binary Trees, DFS commonly appears in three variants:
#
#   1. Inorder   (Left -> Root -> Right)
#   2. Preorder  (Root -> Left -> Right)
#   3. Postorder (Left -> Right -> Root)
#
# Below we:
#   - Define a Binary Search Tree (BST)
#   - Insert values into it
#   - Implement all three DFS traversals
#   - Test the traversal algorithm
# --------------------------------------

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.info:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)

        if value > node.info:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)


# ---------------------------------------------
# DFS Traversal Algorithms
# ---------------------------------------------

def preorder(root):
    """
    Preaorder DFS: 
    Root -> Left -> Right
    Useful for copying or serializing a tree.
    """
    if root is None:
        return []
    
    return [root.info] + preorder(root.left) + preorder(root.right)

def inorder(root):  
    """ 
    Inorder DFS: 
    Left -> Root -> Right 
    For a BST, this returns values in sorted order.
    """
    if root is None:
        return []

    return inorder(root.left) + [root.info] + inorder(root.right)

def postorder(root):
    """
    Postorder DFS:
    Left -> Right -> Root
    Ofthen userd for deleting.
    """
    if root is None:
        return []
    
    return postorder(root.left) + postorder(root.right) + [root.info]
    

# ---------------------------------------------
# Tests
# ----------------------------------------------

if __name__ == '__main__':
    """
    Construct the following BST:

            8
          /   \
         3     10
        / \      \
       1   6      14
          / \     /
         4   7   13

    Inorder:
        inorder(4) = inorder(2) + [4] + inorder(6)
        inorder(2) = inorder(1) + [2] + inorder(3)

    Postorder:
        postorder(3) = postorder(1) + postorder(6) + [3]
        postorder(6) = postorder(4) + postorder(7) + [6]
    """

    bst = BinarySearchTree()
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

    for v in values:
        bst.insert(v)

    print("Preorder Traversal:")
    print(preorder(bst.root))       # [8, 3, 1, 6, 4, 7, 10, 14, 13]

    print("Inorder Traversal:")
    print(inorder(bst.root))        # [1, 3, 4, 6, 7, 8, 10, 13, 14]

    print("Postorder Traversal:")
    print(postorder(bst.root))      # [3, 1, 6, 4, 7, 10, 14, 13, 8]
