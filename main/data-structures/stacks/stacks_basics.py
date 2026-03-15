""" STACKS - BASICS
-------------------
A stack is a collection of items with restricted access:
  - You can only add items to the TOP
  - You can only remove items from the TOP

This rule is called LIFO:
  - Last In, First Out

It is like:
  - A stack of plates  
  - Browser back history
  - Undo/Redo in an editor 

You can't remove the middle item or inspect everything freely.

Python does not have a special Stack type,
but lists already support stack behavior.

List methods:
  - append() -> push to top (end)
  - pop() -> remove from top (end)

Example: Undo user action
-------------------------
"""

# Stack to store user actions
undo_stack = []

# User performs actions
undo_stack.append("Type Hello")
undo_stack.append("Type World")
undo_stack.append("Delete World")

# Current actions stack
print("Current stack:", undo_stack)  # ['Type Hello', 'Type World', 'Delete World']

# User presses Undo
last_action = undo_stack.pop()
print("Undo action:", last_action)  # Undo action: Delete World

# Current actions stack
print("Current stack:", undo_stack) # ['Type Hello', 'Type World']