""" A Frame contain information about a single function call.
Frames are created and pushed onto the stack when function is called.
When the function returns, that frame is popped off the stack.
"""

# Frame's number
no = 0

def A():
   global no
   no += 1

   i = no
   print(f"Function A / Frame {i}")

   # Push anew frame onto the stack
   B()

   print(f"Function A / Frame {i}")
   return

def B():
   global no
   no += 1

   print(f"Function B / Frame {no}")
   return


# Push first frame onto the stack (function call)
A()

# Push new frame onto the stack
B()

"""
   Function A / Frame 1
   Function B / Frame 2
   Function A / Frame 1
   Function B / Frame 3
"""