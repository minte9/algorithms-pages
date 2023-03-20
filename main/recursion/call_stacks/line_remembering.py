""" 
Programming languages remembers the line of code that 
called a function and returns to that line when the function 
finishises its execution.
"""

def a():
    print('a()'); b()
    print('return a')

def b():
    print('b()'); c()
    print('return b')

def c():
    print('c()')
    print('return c')

a()

"""
    a()
    b()
    c()
    return c
    return b
    return a
"""