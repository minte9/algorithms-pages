""" Minimax algorithm - Dummy 3
Binary tree with arbitrary number of children.
"""

def minimax(node, player):

    if isinstance(node, int): # Base case
        return node
    
    value = float("-inf") if player else float("+inf")

    for k in node:
        sub_val = minimax(k, not player) # Recursive case

        if player:
            value = max(sub_val, value) 
        else:
            value = min(sub_val, value) 

    return value

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