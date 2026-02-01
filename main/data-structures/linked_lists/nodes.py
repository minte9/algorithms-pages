# NODES - Building Blocks of a Linked List
# ----------------------------------------
#
# A Node is a small container that holds:
#   - data (the actual value)
#   - nextNode (a reference to the next node in memory)
#
# Important:
#   - nodes are NOT stored next to each other in memory
#   - each node only knows where the NEXT node is
#   - this is why we must follow the links step by step
# 
# Real-life analogy:
# A treasure hunt clue that less you:
#   - the message
#   - where the next clue is
# --------------------------

class Node:
    def __init__(self, data):
        self.data = data        # The value stored in the node
        self.next = None        # Reference to the next node


# Example: Manual Node Linking
# ----------------------------

node1 = Node("Go to the oak tree")
node2 = Node("Look under the bench")
node3 = Node("Check the fountain")

node1.next = node2
node2.next = node3

print(node1.data, '->', node1.next.data)
print(node2.data, '->', node2.next.data)

# ------------------------------------------
# Go to the oak tree -> Look under the bench
# Look under the bench -> Check the fountain