""" Minimax algorithm - Dummy 
Binary tree, with only two choices, left and right.

The tree will have nodes that branch out, and it will have 
leafs with fixed values. 

We go down the tree in order to find the best choises.
The algoritm defined to accept a Boolean flag (which one is playing).

When it's max player turn, the algorithm is trying to maximize the score.
When it's min player turn, the algorithm is trying to minimize the score.

We use `not player` when calling minimax recursively to switch 
back and forth between the players.
"""

def minimax(node, player, i=0):
    
    if isinstance(node, list):
        print("  " * i, "Node", node)

        lv = minimax(node[0], not player, i=i+1) # Recursive case
        rv = minimax(node[1], not player, i=i+1)

        if player:
            best_score = max(lv, rv)
        else:
            best_score = min(lv, rv)

        print("   " * i, "Player", player, "Best score:", best_score)
        return best_score

    # print("  " * i, "Leaf:", node) # Base case
    return node


tree = [[9, 5], [-3, -2]]

print("Player True")
print("Best score =", minimax(tree, True), '\n')

print("Player False:")
print("Best score =", minimax(tree, False), '\n')

"""

Player True
 Node [[9, 5], [-3, -2]]
   Node [9, 5]
    Player False Best score: 5
   Node [-3, -2]
    Player False Best score: -3
 Player True Best score: 5
Best score = 5

Player False:
 Node [[9, 5], [-3, -2]]
   Node [9, 5]
    Player True Best score: 9
   Node [-3, -2]
    Player True Best score: -2
 Player False Best score: -2
Best score = -2

"""