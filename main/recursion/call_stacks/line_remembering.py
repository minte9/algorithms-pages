""" Programming languages remembers the line of code that 
called a function and returns to that line when the function 
finishises its execution.
"""

def first_function():
    print('Line 07')
    
    second_function()

    print('Line 09 - return to first function')
    return

def second_function():
    print('Line 10')
    return

first_function()

"""
    Line 07
    Line 10
    Line 09 - retrun to first function
"""