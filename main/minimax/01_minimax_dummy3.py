""" Minimax algorithm - Dummy 4
Binary tree with arbitrary number of children.
With comments and statements.
"""

def minimax(node, player, i=0):
    if isinstance(node, int): 
        print("  Value:", node)
        return node

    max_ = float("-inf") # negative infinity
    min_ = float("+inf")

    if player:
        for k in node:
            child_score = minimax(k, not player, i+1)
            max_ = max(child_score, max_)
            print(" " * i, f"Maximizing: child score = {child_score}, max so far = {max_}")
        return max_
    
    else:
        for k in node:
            child_score = minimax(k, not player, i+1)
            min_ = min(child_score, min_)
            print(" " * i, f"Minimizing: child score = {child_score}, min so far = {min_}")
        return min_

    return result

tree = [
    [
        [
            [3, 4]
        ],
        [
            8,
            [-2, 10], 
            5,
        ],
    ],
    7,
]


print(tree, '\n')

print("Max player:")
print("Result:", minimax(tree, True))
print()

print("Min player:")
print("Result:", minimax(tree, False))
print()


"""
[[[[3, 4]], [8, [-2, 10], 5]], 7]

Max player:
  Value: 3
    Minimizing: child score = 3, min so far = 3
  Value: 4
    Minimizing: child score = 4, min so far = 3
   Maximizing: child score = 3, max so far = 3
  Minimizing: child score = 3, min so far = 3
  Value: 8
   Maximizing: child score = 8, max so far = 8
  Value: -2
    Minimizing: child score = -2, min so far = -2
  Value: 10
    Minimizing: child score = 10, min so far = -2
   Maximizing: child score = -2, max so far = 8
  Value: 5
   Maximizing: child score = 5, max so far = 8
  Minimizing: child score = 8, min so far = 3
 Maximizing: child score = 3, max so far = 3
  Value: 7
 Maximizing: child score = 7, max so far = 7
Result: 7

Min player:
  Value: 3
    Maximizing: child score = 3, max so far = 3
  Value: 4
    Maximizing: child score = 4, max so far = 4
   Minimizing: child score = 4, min so far = 4
  Maximizing: child score = 4, max so far = 4
  Value: 8
   Minimizing: child score = 8, min so far = 8
  Value: -2
    Maximizing: child score = -2, max so far = -2
  Value: 10
    Maximizing: child score = 10, max so far = 10
   Minimizing: child score = 10, min so far = 8
  Value: 5
   Minimizing: child score = 5, min so far = 5
  Maximizing: child score = 5, max so far = 5
 Minimizing: child score = 5, min so far = 5
  Value: 7
 Minimizing: child score = 7, min so far = 5
Result: 5
"""