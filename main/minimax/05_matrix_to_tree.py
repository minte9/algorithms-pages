""" Matrix list to tree
Tree with arbitrary number of children
"""

class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

def matrix_to_tree(m):
    if isinstance(m, int):
        return Node(m, [])

    children = [matrix_to_tree(child) for child in m]
    return Node(None, children)

matrix = [
    [
        [3, 4],
        [8, [-2, 10], 5],
    ],
    7,
]

tree = matrix_to_tree(matrix)
assert tree.children[0].children[0].children[0].value == 3
assert tree.children[0].children[0].children[1].value == 4
assert tree.children[0].children[1].children[0].value == 8
assert tree.children[0].children[1].children[1].children[0].value == -2

matrix = [
    [3, 4],
    [8, [-2, 10], 5],
    7,
]

tree = matrix_to_tree(matrix)
assert tree.children[0].children[0].value == 3
assert tree.children[0].children[1].value == 4
assert tree.children[1].children[0].value == 8
assert tree.children[1].children[1].children[0].value == -2
assert tree.children[1].children[1].children[1].value == 10
assert tree.children[2].value == 7