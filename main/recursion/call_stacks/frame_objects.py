""" Frame objects

A Frame contain information about a single function call.
Frames are created and pushed onto the stack when function is called.

When the function returns, that frame is popped off the stack, 
and the previous frame object becomes the current one, 
resuming the execution of the calling function from where it left off.
"""

def frame_objects(i=1):
   print('A Frame', 'No.', i)
   second_func(i+1)
   print('A Frame', 'No.', i)
   return

def second_func(i):
   print('B Frame', 'No.', i)
   third_func(i+1)
   print('B Frame', 'No.', i)
   return

def third_func(i):
   print('C Frame', 'No.', i)
   return

frame_objects()

"""
   A Frame No. 1
   B Frame No. 2
   C Frame No. 3
   B Frame No. 2
   A Frame No. 1
"""