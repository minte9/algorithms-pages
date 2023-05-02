""" Minimax algorithm - Dummy
Binary tree, with only two choices, left and right.

When is Max turn on list node, we evaluate each node children
on `not player` choise, because Min player will try to minimize
the Max score.
"""

def minimax(node, player):
    if isinstance(node, int):  # Base case
        return node

    lv = minimax(node[0], not player) # Recursive
    rv = minimax(node[1], not player) # Recursive

    if player:
        best_score = max(lv, rv)
    else:
        best_score = min(lv, rv)
        
    return best_score

tree = [[9, 5], [-3, -2]]

print('Max to play / Best score =', minimax(tree, True))
print('Min to play / Best score =', minimax(tree, False))

# Max to play =  5
# Min to play = -2