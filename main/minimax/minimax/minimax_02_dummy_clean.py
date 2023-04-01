""" Minimax algorithm - Dummy 2
Binary tree, with only two choices, left and right.
Refactoring.
"""

def minimax(node, player):
    if isinstance(node, int): 
        return node

    lv = minimax(node[0], not player)
    rv = minimax(node[1], not player)

    if player:
        result = max(lv, rv)
    else:
        result = min(lv, rv)
        
    return result

tree = [[9, 5], [-3, -2]]

print('Max to play =', minimax(tree, True))
print('Min to play =', minimax(tree, False))

# Max to play =  5
# Min to play = -2