""" Programming languages remembers the line of code that 
called a function and returns to that line when the function 
finishises its execution.
"""

def a():
    print('a - Line 07'); b()
    print('a - Line 08')
def b():
    print('b - Line 11'); c()
    print('b - Line 12')
def c():
    print('c - Line 13')
    print('c - Line 14')
a()

"""
a - Line 07
b - Line 11
c - Line 13
c - Line 14
b - Line 12
a - Line 08
"""