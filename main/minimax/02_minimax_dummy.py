""" Minimax algorithm
Dumny binary tree (two choices - left, right)

We go down the tree in order to find the best moves.
The algoritm defined to accept a Boolean flag (which one is playing) 

Algorithm, recursion down the tree
"""

class Choise:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Point:
    def __init__(self, value):
        self.val = value

def opponent(player=True):
    return not player

def minimax(tree, player, i=0):
    if isinstance(tree, Point):
        print(" " * i, "Value:", tree.val) # return node value
        return tree.val

    # Call recursively on children
    left  = minimax(tree.left,  opponent(player), i=i+1)
    right = minimax(tree.right, opponent(player), i=i+1)

    if player:
        print("  " * i, "Player", player, "/ Choise node")
        print("    " * i, "Max:", max(left, right)) # Max player turn
        return max(left, right)
    else:
        print("  " * i, "Player", player, "/ Choise node")
        print("    " * i, "Min:", min(left, right)) # Min player turn
        return min(left, right)


tree = Choise(
    Choise(
        Point(9),
        Point(5),
    ),
    Choise(
        Point(-3),
        Point(-2),
    )
)

print("-----------------------------------")
print("Max player:")
print("Result:", minimax(tree, True))
print("-----------------------------------")
print("Min player:")
print("Result:", minimax(tree, False))
print("-----------------------------------")


"""
-----------------------------------
Max player:
 Player True / Options node
   Player False / Options node
   Value: 9
   Value: 5
     Min: 5
   Player False / Options node
   Value: -3
   Value: -2
     Min: -3
 Max: 5
Result: 5
-----------------------------------
Min player:
 Player False / Options node
   Player True / Options node
   Value: 9
   Value: 5
     Max: 9
   Player True / Options node
   Value: -3
   Value: -2
     Max: -2
 Min: -2
Result: -2
-----------------------------------
"""