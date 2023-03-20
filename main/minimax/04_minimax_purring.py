""" Minimax algorithm - Prunning
Code refactoring
"""

class Tree:
    def __init__(self, children):
        self.children = children
    
    def __str__(self):
        return f"[{', '.join(str(sub) for sub in self.children)}]"

class Point(Tree):
    def __init__(self, value):
        super().__init__([]) # point is a Tree with no children
        self.val = value

    def __str__(self):
        return f"{self.val}"

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

    print(tree)    
    v, f = (float("-inf"), max) if player else (float("+inf"), min)
    for sub in tree.children:
        v = f(minimax(sub, not player), v)
    return v

def prunning(tree, player, alpha=float("-inf"), beta=float("+inf")):
    if isinstance(tree, Point): 
        return tree.val
    
    print(tree)
    v = float("-inf") if player else float("+inf")
    for sub in tree.children:
        sub_val = prunning(sub, not player, alpha, beta)

        # prunning
        if (player): 
            v = max(sub_val, v)
            alpha = max(alpha, v)
            if (v >= beta): break
        else:
            v = min(sub_val, v)
            beta = min(beta, v)
            if (v <= alpha): break

    return v

print(minimax(tree, True))  # 7
print(prunning(tree, True)) # [-2, 10] is ignored