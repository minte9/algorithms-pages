""" The code in a recursive call can be split in two partes, 
before the recursive call and after recursive call.
Reaching the base case doesn't necessary means the end 
of the recursive algorithm.
"""

def a(n):
    print('Before', '\t', 'n =', n)

    if n == 0:
        print('Base', '\t', 'n =', n)
        return

    a(n-1) # recursive call

    print('After', '\t', 'n =', n)
    return

a(2)

"""
    Before   n = 2
    Before   n = 1
    Before   n = 0
    Base     n = 0
    After    n = 1
    After    n = 2
"""