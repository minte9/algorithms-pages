# CUSTOM QUEUE
#-------------
# Queue isn't implemented in many programming language.
# We create a queue to see how it works internally.
# (Educational purpose)
# ---------------------

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add item to the back of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove item from the front of the queue
        if not self.items:
            return None
        return self.items.pop(0)

    def peek(self):
        # Read first item without removing it
        if not self.items:
            return None
        return self.items[0]

    def __str__(self):
        return str(self.items)
    
# 1) Create queue
# ---------------
queue = Queue()

# 2) Add elements
# ---------------
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)  # [1, 2, 3]

# 3) Remove from front
# --------------------
removed = queue.dequeue()

print("Removed:", removed)
print("Queue:", queue)
print("New front:", queue.peek())

# ----------
# Removed: 1
# Queue: [2, 3]
# New front: 2