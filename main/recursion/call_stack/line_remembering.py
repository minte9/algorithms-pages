""" Programming languages remember the line of code that called a function. 
It returns to that line when the function finishes its execution.
"""

def A():
    print('A -> Line 01')

    
    print('A -> Goto B and remember the line in A')
    B()

    print('A -> Line 02');

def B():
    print('B -> Line 01')

A()

"""
    A -> Line 01
    A -> Goto B and remember the line in A
    B -> Line 01
    A -> Line 02
"""