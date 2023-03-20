""" Base cases
To avoid a crash, there must be a base case, where function
stop calling itself and just returns.

All recursive function require at least on base case and 
at least one recursive case.
"""

def a(repeat, i=0):
    i = i  + 1
    print('Frame', i, 'a(repeat=%s) called' % repeat)

    if not repeat: # Base case
        print('Frame', i, 'Base case')
        return

    a(False, i) # Recursive case
    print('Frame', i, 'Recursive case')
    return
    
a(True)

"""
    Frame 1 a(repeat=True) called
    Frame 2 a(repeat=False) called
    Frame 2 Base case
    Frame 1 Recursive case
"""