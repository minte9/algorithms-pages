""" Programming languages remembers the line of code that 
called a function and returns to that line when the function 
finishises its execution.
"""

def a():
    print('A - Line 07'); b()
    print('A - Line 08')
def b():
    print('B - Line 11'); c()
    print('B - Line 12')
def c():
    print('C - Line 13')
    print('C - Line 14')
a()

"""
A - Line 07
B - Line 11
C - Line 13
C - Line 14
B - Line 12
A - Line 08
"""