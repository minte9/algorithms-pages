# CUSTOM STACK - TYPE
#--------------------
# Most languages do not provide stacks, so we create our own.
# This is good for enforcing rules and readability.
#
# With a raw list, this is posible:
#   stack = [1, 2, 3]
#   stack.insert(0, 99)  # breaks stack rules
#   stack[1] = 42        # breaks stack rules 
# 
# With a Stack class:
#   stack.push(1)
#   stack.push(2)
#   stack.push(3)       # no way to touch the middle
# 
# Example:
#   - Undo functionality
# ----------------------

class Stack:
    def __init__(self):
        self.items = []  # Internal storage

    def push(self, item):
        self.items.append(item)  # Add item to top of stack

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()  # Remove and return top item
    
    def peek(self):
        if not self.items:
            return None
        return self.items[-1] # Read top item without removing it
    
# Create stack
undo_stack = Stack()

# Add actions
undo_stack.push("Type: Hello")
undo_stack.push("Type: World")
undo_stack.push("Delete: World")

# Undo last action
undo_stack.pop()

# New top
print("Top:", undo_stack.peek())
print("Stack:", undo_stack.items)

# -------------------------------------
# Top: Type: World
# Stack: ['Type: Hello', 'Type: World']