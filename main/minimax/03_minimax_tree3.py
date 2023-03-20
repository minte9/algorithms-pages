""" Minimax algorithm
Tree with arbitrary number of children
Code refactoring, matrix to tree
"""

class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

def matrix_to_tree(x):
    if isinstance(x, int):
        return Node(x, [])

    children = [matrix_to_tree(child) for child in x]
    return Node(None, children)

matrix = [
    [
        [3, 4],
        [8, [-2, 10], 5],
    ],
    7,
]

# Convert matrix to a tree of Nodes
tree = matrix_to_tree(matrix)
assert tree.children[0].children[0].children[0].value == 3
assert tree.children[0].children[1].children[1].children[0].value == -2
assert tree.children[1].value == 7

# Minimax algorithm
def minimax(tree, player):
    if tree.children == []: # is leaf
        return tree.value

    if player:
        max_ = float("-inf")
        for k in tree.children:
            max_ = max(minimax(k, not player), max_)
        return max_

    else:
        min_ = float("+inf")
        for k in tree.children:
            min_ = min(minimax(k, not player), min_)
        return min_

print(minimax(tree, True))  # 7
print(minimax(tree, False)) # 5