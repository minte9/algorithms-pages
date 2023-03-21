""" Frame objects
The program's call stacks, is a stack of frame objects.
Frame objects contain information about a single function call.

Frames are created and pushed onto the stack when function is called.
When the function returns, that frame is popped off the stack.

Variables are always separate variables,
even if they have the same name as local variables in functions.

Every running program has a call stack, 
and multithreaded programs have one call stack for each thread.

The fact that the call stack doesn't exist in the code makes 
the recursion so confusing for beginners.
"""

def a():
   x = '10'
   print('Frame A: x =', x); b()
   print('Frame A: x =', x)

def b():
   x = '20'
   print('Frame B: x =', x); c()
   print('Frame B: x =', x)

def c():
   x = '30'
   print('Frame C: x =', x)

a()

"""
    Frame A: x = 10
    Frame B: x = 20
    Frame C: x = 30
    Frame B: x = 20
    Frame A: x = 10
"""