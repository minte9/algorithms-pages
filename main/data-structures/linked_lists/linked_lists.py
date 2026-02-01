# LINKED LIST - Structure & Operations
# ------------------------------------
#
# Concept:
#   - Keep track ONLY of the first node
#   - Traverses nodes by following next references
#   - Has no direct access by index (unlike arrays)
#
# Time Complexity:
#   - Read (by index): O(n)
#   - Insert at beggining: O(1)
#   - Insert elsewhere: O(n)
#
# Below:
#   - Linked list that stores a reference to the first node.
# ----------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
   
class LinkedList:
    def __init__(self, first):
        self.first = first

    # --------------------------
    # READ value at index / O(n)
    # --------------------------
    def read(self, index):
        current = self.first
        i = 0

        while i < index:
            current = current.next
            i += 1

        return current
    
    # ----------------------------
    # INSERT value at index / O(n)
    # ----------------------------
    def insert(self, index, value):
        node = Node(value)

        # Insert at the beginning / O(1)
        if index == 0:
            node.next = self.first
            self.first = node
            return
        
        # Insert elsewhere / O(n)
        current = self.first
        i = 0

        # Stop at node BEFORE insertion point
        while i < index - 1:
            current = current.next
            i += 1

        node.next = current.next
        current.next = node


# ---------------------
# Example Usage & Tests
# ---------------------

# Create nodes
n1 = Node("Start")
n2 = Node("Forest")
n3 = Node("River")
n4 = Node("Treasure")

# Link nodes
n1.next = n2
n2.next = n3
n3.next = n4

# Create linked list
hunt = LinkedList(n1)

# Insert new nodes
hunt.insert(0, "Map")
hunt.insert(3, "Cave")

# Read nodes
print(hunt.read(0).data)  # Map
print(hunt.read(1).data)  # Start
print(hunt.read(2).data)  # Forest
print(hunt.read(3).data)  # Cave
print(hunt.read(4).data)  # River
print(hunt.read(5).data)  # Treasure