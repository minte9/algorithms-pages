""" Stack overflow
A recurson function is a function that calls itself.

The limit of calls is called maximum recursion depth.
For Python, this size is set to 1000.

Stack overflows don't damage the computer, 
it just terminatet the program.
"""

def repeat():
    repeat()

repeat() 
    # RecursionError: maximum recursion depth exceeded