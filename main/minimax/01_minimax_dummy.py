""" Minimax algorithm - Dummy 1
Binary tree, with only two choices, left and right.

The tree will have nodes that branch out, and it will have 
leafs with fixed values. 

We go down the tree in order to find the best moves.
The algoritm defined to accept a Boolean flag (which one is playing).

When it's max player turn, the algorithm is trying to maximize the score.
When it's min player turn, the algorithm is trying to minimize the score.

We use `not player` when calling minimax recursively to switch 
back and forth between the players.
"""

def minimax(node, player, i=0):
    
    if isinstance(node, list):
        lv = minimax(node[0], not player, i=i+1) # Recursive case
        rv = minimax(node[1], not player, i=i+1)

        if player:
            result = max(lv, rv)
        else:
            result = min(lv, rv)

        print("  " * i, "Player =", player, "/ choise:", result)
        return result

    print(" " * i, "Value:", node) # Base case
    return node


tree = [[9, 5], [-3, -2]]

print("Player = True:")
print("Result:", minimax(tree, True))
print()

print("Player = False:")
print("Result:", minimax(tree, False))
print()

"""
Player = True:
   Value: 9
   Value: 5
   Player = False / Min choise: 5
   Value: -3
   Value: -2
   Player = False / Min choise: -3
 Player = True / Max choise 5
Result: 5

Player = False:
   Value: 9
   Value: 5
   Player = True / choise: 9
   Value: -3
   Value: -2
   Player = True / choise: -2
 Player = False / choise: -2
Result: -2
"""