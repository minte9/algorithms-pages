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

# Algorithm
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

""" Game state A (draw)
    X 0 X
    X 
    O   0
"""
endgame_leafs = [
    [[0], [0]],
    [ -1, [0]],
    [ -1, [0]],
]
tree = matrix_to_tree(endgame_leafs)
print(minimax(tree, True))  # 0
print(minimax(tree, False)) # 0

""" Game state B (O wins)
    X    
    X 0 X
    O   0
"""
endgame_leafs = [
    [-1,  -1],
    [-1, [0]],
    [-1, [0]],
]
tree = matrix_to_tree(endgame_leafs)
print(minimax(tree, True))  # -1
print(minimax(tree, False)) # -1