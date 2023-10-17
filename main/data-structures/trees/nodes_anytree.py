from anytree import Node, RenderTree

root = Node('A')
node2 = Node('B', parent=root)
node3 = Node('C', parent=root)
node4 = Node('D', parent=node2)
node5 = Node('E', parent=node3)
node6 = Node('F', parent=node3)
node7 = Node('G', parent=node5)
node8 = Node('H', parent=node5)

print("Tree:")
for pre, fill, node in RenderTree(root):
    print(pre, node.name)

# Delete node 'C' and its descendants
node3.parent = None

print("Tree after deletion:")
[print(pre,node.name) for pre,_,node in RenderTree(root)]

"""
    Tree:
    A
    ├──  B
    │   └──  D
    └──  C
        ├──  E
        │   ├──  G
        │   └──  H
        └──  F
    Tree after deletion:
    A
    └──  B
        └──  D
"""