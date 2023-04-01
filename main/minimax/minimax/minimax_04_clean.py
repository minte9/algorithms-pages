""" Minimax algorithm - Dummy 3
Binary tree with arbitrary number of children.
"""

def minimax(node, player):

    if isinstance(node, int): # Base case
        return node
    
    val, func = (float("-inf"), max) if player else (float("+inf"), min)

    for k in node:
        val = func(minimax(k, not player), val) # Recursive case

    return val

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