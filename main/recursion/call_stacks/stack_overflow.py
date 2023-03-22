""" Stack overflow
The limit of calls is called maximum recursion depth.
Stack overflows don't damage the computer, it just terminatet the program.
For Python, this size is set to 1000.
"""

def repeat():
    repeat()

repeat() 
    # RecursionError: maximum recursion depth exceeded