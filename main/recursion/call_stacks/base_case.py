""" Base case 
To avoid a crash, there must be a base case, where function
stop calling itself and just returns.
The code in a recursive call can be split in two parts, 
before the recursive call and after recursive call.
"""

def show_frame(repeat, i=0):
    i = i  + 1

    print('Frame', i, '- repeat = ' + str(repeat))

    if repeat == False:
        print('Frame', i, '- return / Base case')
        return

    show_frame(False, i)
    
    print('Frame', i, '- return / Recursive case')
    return

def show_before_after(n):
    print('Before', '\t', 'n =', n)

    if n == 0:
        print('Base', '\t', 'n =', n)
        return

    show_before_after(n-1) # recursive call

    print('After', '\t', 'n =', n)
    return
 
show_frame(True)
show_before_after(2)

"""
    Frame 1 - repeat = True
    Frame 2 - repeat = False
    Frame 2 - return / Base case
    Frame 1 - return / Recursive case
    Before   n = 2
    Before   n = 1
    Before   n = 0
    Base     n = 0
    After    n = 1
    After    n = 2
"""