# BREADTH-FIRST SEARCH (BFS) TRAVERSAL
# ------------------------------------
#
# BFS traversal visits nodes level by level.
#   - First the root
#   - Then all nodes at depth 1 (children of root)
#   - Then all nodes at depth 2, and so on
#
# To achive this, we use a QUEUE (FIFO):
#   - Enque children as we visit nodes
#   - Dequeue nodes in the order they were discovered
#
# This example includes:
#   - Binary Search Tree implementation
#   - Tree population
#   - BFS traversal
#   - Simple test cases
# ----------------------------------------------------

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
# CONSTRUCT THE TREE
# ---------------------------------------------

bst = BinarySearchTree()
values = [10, 5, 15, 3, 7, 12, 18]

for v in values:
    bst.insert(v)

    """
            10
          /   \
         5     15
        / \    /  \
       3   7  12  18
    """


# ---------------------------------------------
# BFS / LEVEL ORDER TRAVERSAL
# ---------------------------------------------

def bfs_traversal(root):
    """
    Perform BFS (Lever Order Traversal) on a binary tree.
    Returns:
        - A list of values in BFS order.

    Time complexity:
        - Lists make this O(n) due to shifting, resulting in O(n^2).
        - Using deque.popleft() keeps BFS at O(n).
    """ 
    if root is None:
        return []
    
    queue, result = [], []

    # Start with the root node
    queue.append(root)

    while queue:
        # Deque the first element
        node = queue.pop(0)

        # Visit the node
        result.append(node.info)

        # Enqueue left child
        if node.left:
            queue.append(node.left)

        # Enqueue right child
        if node.right:
            queue.append(node.right)

    return result


# ---------------------------------------------
# TESTS
# ---------------------------------------------

print("Test 1 - BFS Traversal:")
print(bfs_traversal(bst.root))  # [10, 5, 15, 3, 7, 12, 18]

# --------------------------------------
#   Step    Queue               Output
# --------------------------------------
#   1       [5, 15]             [10]  
#   2       [15, 3, 7]          [10, 5]         
#   3       [3, 7, 12, 18]      [10, 5, 15]
#   4       [7, 12, 18]         [10, 5, 15, 3]
#   5       [12, 18]            [10, 5, 15, 3, 7]
#   6       [18]                [10, 5, 15, 3, 7, 12]
#   7       []                  [[10, 5, 15, 3, 7, 12, 18]