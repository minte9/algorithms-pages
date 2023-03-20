""" Recursive case
Returning from base case doesn't immediately return
from all the recursive calls that happend before it.

The code in a recursive call can be split in two partes:
the code before and the code after.
"""

def a(n):
    print(n)
    if n == 0:
        print('Base case')
        return

    a(n-1)
    print(n, 'returning')
    return

a(3)

"""
    3
    2
    1
    0
    Base case
    1 returning
    2 returning
    3 returning
"""