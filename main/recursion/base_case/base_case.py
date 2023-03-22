""" To avoid a crash, there must be a base case, where function
stop calling itself and just returns.
All recursive function require at least on base case and 
at least one recursive case.
"""

def a(repeat, i=0):
    i = i  + 1
    print('Frame', i, '- repeat = ' + str(repeat))

    if not repeat:
        print('Frame', i, '- return / Base case')
        return

    a(False, i)
    print('Frame', i, '- return / Recursive case')
    return
    
a(True)

"""
    Frame 1 - repeat = True
    Frame 2 - repeat = False
    Frame 2 - return / Base case
    Frame 1 - return / Recursive case
"""