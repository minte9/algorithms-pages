""" The code in a recursive call can be split in two partes, 
before the recursive call and after recursive call.
Reaching the base case doesn't necessary ends the program.
"""

def a(n):
    print(n)

    if n == 0:
        print('Base case'); return

    a(n-1)
    print(n, 'returning'); return

a(2)

"""
    2
    1
    0
    Base case
    1 returning
    2 returning
"""