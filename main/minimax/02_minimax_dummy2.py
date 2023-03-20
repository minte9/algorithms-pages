""" Minimax algorithm (refactoring)
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

def minimax(tree, player):
    if isinstance(tree, Point):
        return tree.val

    lv = minimax(tree.left,  not player) # left value (for opponent)
    rv = minimax(tree.right, not player) # right value (for opponent)
    if player:
        return max(lv, rv)
    else:
        return min(lv, rv)

tree = Choise(
    Choise(
        Point(0),  
        Point(0)),
    Choise(
        Point(-2), 
        Point(-1)),
)

print(minimax(tree, True))  # 0
print(minimax(tree, False)) # -1