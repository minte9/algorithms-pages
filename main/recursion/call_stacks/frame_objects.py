""" Frame objects
A Frame contain information about a single function call.
Frames are created and pushed onto the stack when function is called.
When the function returns, that frame is popped off the stack.

Variables are always separate variables,
even if they have the same name as local variables in functions.
"""

def first():
   x = '10'
   print('Frame A: x =', x); second()
   print('Frame A: x =', x)

def second():
   x = '20'
   print('Frame B: x =', x); third()
   print('Frame B: x =', x)

def third():
   x = '30'
   print('Frame C: x =', x)

first()

"""
    Frame A: x = 10
    Frame B: x = 20
    Frame C: x = 30
    Frame B: x = 20
    Frame A: x = 10
"""