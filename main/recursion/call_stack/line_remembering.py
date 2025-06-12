""" Programming languages remembers the line of code that called a function. 
It returns to that line when the function finishes its execution.
"""

def A():
    print('Line 01 in A')

    
    # Go to B and remember the line
    B()

    print('Line 02 in A');

def B():
    print('Line 01 in B')

A()

"""
    Line 01 in A
    Go to B
    Line 01 in B
    Line 02 in A
"""