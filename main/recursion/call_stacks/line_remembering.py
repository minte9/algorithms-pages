""" Code line remembering
All programming languages remembers which line of code 
called the function and returns to it when the function 
finishises its execution.
"""

def a():
    print('a() called')
    b()
    print('a() is returning')

def b():
    print('b() called')
    c()
    print('b() is returning')

def c():
    print('c() called')
    print('c() is returning')

a()

"""
    a() called
    b() called
    c() called
    c() is returning
    b() is returning
    a() is returning
"""