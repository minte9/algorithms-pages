# LINKED LIST - INSERT AT TAIL
# ----------------------------
#
# Concept:
#   - We only store a reference to the FIRST node (head)
#   - Nodes know ONLY about the next node
#   - To insert at the tail, we must traverse the list
# 
# Key Insights:
#   - Assigning `current = self.head` does NOT copy the node
#   - `current` and `self.head point` to the SAME object
#   - Moving `current` does not move `self.head`
#   - Modifying the `current.next` MUTTATES the list itself (!)
# 
# Time Complexity:
#   - Insert at tail: O(n)
# # ----------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_tail(self, value):
        new_node = Node(value)

        # -------------------------------------
        # Case 1: Empty list
        # The new node becames the first (head)
        # -------------------------------------
        if self.head is None:
            self.head = new_node

        # -----------------------------
        # Case 2: Non-empty list
        # Start traversal from the head
        # -----------------------------
        current = self.head

        # ---------------------------------------------
        # Move `current` until it reaches the last node
        # (the node whose `next` is None)
        # ---------------------------------------------
        while current.next is not None:
            current = current.next

        # ------------------------------------------------
        # We mutate the last node, extending the list that 
        # `self.head` already points to. 
        # ------------------------------------------------
        current.next = new_node


# ---------------------
# Example Usage & Tests
# ---------------------

# Create nodes
n1 = Node("Start")
n2 = Node("Forest")
n3 = Node("River")

# Link nodes
n1.next = n2
n2.next = n3

# Create linked list
hunt = LinkedList(n1)

# Insert at tail
hunt.insert_at_tail("Cave")
hunt.insert_at_tail("Treasure")

# Traverse and print
current = hunt.head
while current:
    print(current.data)
    current = current.next

    # --------------------
    # Start
    # Forest
    # River
    # Cave
    # Treasure
