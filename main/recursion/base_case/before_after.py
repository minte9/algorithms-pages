""" The code in a recursive call can be split in two partes, 
before the recursive call and after recursive call.
Reaching the base case doesn't necessary means the end 
of the recursive algorithm.
"""

def a(n):
    print(n, '- Before')
    
    if n == 0:
        print('Base case')
        return

    a(n-1) # recursive call

    print(n, '- After')
    return

a(2)

"""
    2
    1
    0
    Base case
    1 returning
    2 returning
"""