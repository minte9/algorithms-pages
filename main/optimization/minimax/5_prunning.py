""" Minimax algorithm - Alpha beta prunning
This algorithm will hava a lot of work on big trees.
Some parts are irellevant and don't need to be traverse.

When maximising, check if value is too high when compared to beta.
When minimising, check if value is too low when compared to alpha.

When alpha is greater or equal than beta, it means that the current player 
has found a better move in different branch.
"""

def minimax(node, player, alpha=float("-inf"), beta=float("+inf")):
    if isinstance(node, int): 
        return node
    
    print('Node:', node)

    v = float("-inf") if player else float("+inf")
    for k in node:

        sub_val = minimax(k, not player, alpha, beta)

        if (player):
            if sub_val > v: 
                v = sub_val
            alpha = max(alpha, v)
        else:
            if sub_val < v:
                v = sub_val
            beta = min(beta, v)

        # if (player and v >= beta) or (not player and v <= alpha): break

        if alpha >= beta: # pruning condition
            break 

    return v

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

print('Max to play')
move = minimax(tree, True) # [-2, 10] is ignored
print('Max best move =', move, '\n')

print('Min to play')
move = minimax(tree, False)
print('Min best move =', move, '\n')

"""

Max to play
Node: [[[[3, 4]], [8, [-2, 10], 5]], 7]
Node: [[[3, 4]], [8, [-2, 10], 5]]
Node: [[3, 4]]
Node: [3, 4]
Node: [8, [-2, 10], 5]
Max best move = 7

Min to play
Node: [[[[3, 4]], [8, [-2, 10], 5]], 7]
Node: [[[3, 4]], [8, [-2, 10], 5]]
Node: [[3, 4]]
Node: [3, 4]
Node: [8, [-2, 10], 5]
Node: [-2, 10]
Min best move = 5

"""