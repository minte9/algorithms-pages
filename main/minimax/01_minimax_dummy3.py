""" Minimax algorithm - Dummy 3
Binary tree with arbitrary number of children.
"""

def minimax(node, player, i=0):
    if isinstance(node, int): 
        return node

    max_ = float("-inf") # negative infinity
    min_ = float("+inf")

    if player:
        for k in node:
            max_ = max(minimax(k, not player), max_)
        return max_
    
    else:
        for k in node:
            min_ = min(minimax(k, not player), min_)
        return min_

    return result

tree = [
    [
        [
            [3, 4]
        ],
        [
            8,
            [-2, 10], 
            5,
        ],
    ],
    7,
]

print('Max to play =', minimax(tree, True))
print('Min to play =', minimax(tree, False))

# Max to play = 7
# Min to play = 5