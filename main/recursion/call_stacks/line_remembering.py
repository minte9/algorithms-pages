""" Programming languages remembers the line of code that 
called a function and returns to that line when the function 
finishises its execution.
"""

def a():
    print('Line 07')
    b()
    print('Line 09 - return to function a()')

def b():
    print('Line 10')

a()

"""
Line 07
Line 10
Line 09 - retrun to function a()
"""