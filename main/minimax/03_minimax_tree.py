""" Minimax algorithm
Tree with arbitrary number of children
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

def minimax(tree, player):

    if isinstance(tree, Point):
        return tree.val

    if player:
        max_ = float("-inf") # negative infinity
        for k in tree.children:
            max_ = max(minimax(k, not player), max_)
        return max_

    else:
        min_ = float("+inf") # positive infinity
        for k in tree.children:
            min_ = min(minimax(k, not player), min_)
        return min_

print(minimax(tree, True))  # 7
print(minimax(tree, False)) # 5