"""
    This is a staircase of size 4:

    #
    ##
    ###
    ####

    Its base and height are both equal to. 
    It is drawn using # symbols and spaces. 
    The last line is not preceded by any spaces.

    Write a program that prints a staircase of size.
    Print a staircase as described above. No value should be returned.
    The last line is not preceded by spaces. All lines are right-aligned.
"""

def staircase(n):

    for i in range(n):
        print(" "*(n-1-i) + "#" * (i+1))

staircase(4)