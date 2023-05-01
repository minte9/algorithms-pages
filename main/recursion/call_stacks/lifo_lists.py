""" Stacks

A stack stores multiple values like a list. 
Stacks are LIFO data structure (last in, first out)
"""

cards = []
cards.append('5');  print(' '.join(cards))
cards.append('3');  print(' '.join(cards))
cards.append('7');  print(' '.join(cards))
cards.pop();        print(' '.join(cards)) # Last in, First out

"""
    5
    5 3
    5 3 7
    5 3
"""