""" LIFO
A stack stores multiple values like a list. 
Unlike lists, it limits you to adding or removing values only 
from the 'top' of the stack.
Stacks are LIFO data structure (last in, first out)
"""

cards = []
cards.append('5'); print(' '.join(cards))
cards.append('3'); print(' '.join(cards))
cards.append('7'); print(' '.join(cards))

cards.pop()  # Look Here
print(' '.join(cards))

"""
    5
    5 3
    5 3 7
    5 3
"""