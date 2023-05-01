""" Programming languages remembers the line of code 
that called a function. It returns to that line when 
the function finishises its execution.
"""

def line_remembering_function():
    print('Line 08')
    goto()
    
    print('Line 10')
    return

def goto():
    print('Line 14 - return to first function')
    return

line_remembering_function()

"""
    Line 08
    Line 14 - return to first function
    Line 10
"""