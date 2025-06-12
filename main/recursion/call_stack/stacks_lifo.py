""" A stack stores multiple values like a list. 
Stacks are LIFO data structure (last in, first out)
"""

cards = []

# Append cards at the end
cards.append('5'); print(' '.join(cards))
cards.append('3'); print(' '.join(cards))
cards.append('7'); print(' '.join(cards))

# Remove last
cards.pop(); 

# Output the remaining list
print(' '.join(cards)) 

"""
    5
    5 3
    5 3 7
    5 3
"""