""" Minimax algorithm Tree
With comments and statements
"""

class Tree:
    def __init__(self, children):
        self.children = children

class Point(Tree):
    def __init__(self, value):
        super().__init__([]) # point is a Tree with no children
        self.val = value

tree = Tree([
    Tree([
        Tree([
            Tree([
                Point(3), 
                Point(4),
            ])
        ]),
        Tree([
            Point(8),
            Tree([
                Point(-2), 
                Point(10),
            ]),
            Point(5),
        ]),
    ]),
    Point(7),
])

def minimax(tree, player, i=0):

    # If the current node is a point, return its value
    if isinstance(tree, Point):
        print("  Point:", tree.val)
        return tree.val

    # We are on an tree node
    print("Player", player, "/ Tree node")

    # If it's the player's turn, maximize their score
    if player:
        max_ = float("-inf")
        for k in tree.children:
            child_score = minimax(k, not player, i=i+1)
            max_ = max(child_score, max_)
            print(f"    Maximizing: child score is {child_score}, max so far is {max_}")
        return max_

    # Otherwise, minimize the opponent's score
    else:
        min_ = float("+inf")
        for k in tree.children:
            child_score = minimax(k, not player)
            min_ = min(child_score, min_)
            print(f"    Minimizing: child score is {child_score}, min so far is {min_}")
        return min_

print("-----------------------------------")
print("Max player:")
print("Result:", minimax(tree, True))
print("-----------------------------------")
print("Min player:")
print("Result:", minimax(tree, False))
print("-----------------------------------")