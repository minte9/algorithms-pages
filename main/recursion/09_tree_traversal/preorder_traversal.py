""" Tree Traversal
Preorder tree traversal access each node's data before
traversing its child nodes. For example, when you are 
creating a copy of the tree.

Postorder tree traversal traverses a node's child nodes before
accesing the node's data. For example, when deleting a tree and 
ensure that no child node are orphan, by deleting their parent first.
"""

root = {
    'data': 'A', 'children': 
    [
        {
            'data': 'B', 'children': 
            [
                {
                    'data': 'D', 'children': []
                }
            ]
        },
        {
            'data': 'C', 'children': 
            [
                {
                    'data': 'E', 'children': 
                    [
                        {
                            'data': 'G', 'children': []
                        },
                        {
                            'data': 'H', 'children': []
                        }
                    ]
                },
            ]
        },
        {
            'data': 'F', 'children': []
        }
    ]
}

def preorderTraverse(node):
    print(node['data'], end=' ') # Access data before recursion
    if len(node['children']) > 0:
        for child in node['children']:
            preorderTraverse(child) # Recursive Case 
    return # Base Case

def postorderTraverse(node):
    for child in node['children']:
        postorderTraverse(child) # Recursive Case
    print(node['data'], end=' ') # Access data after recursion
    return # Base Case
        
def copyTree(node):
    newcopy = {
        'data': node['data'],
        'children': [],
    }
    if len(node['children']) > 0:
        for child in node['children']:
            children = copyTree(child) # Recursive Case
            newcopy['children'].append(children)  
    return newcopy # Base case

def delTree(node, value):
    for child in node['children']:
        if child['data'] == value:
            node['children'].remove(child) # Remove node
            return True
        if delTree(child, value): # Recursive Case
            return True
    return False # Base case (not found)


print("Traverse /")
preorderTraverse(root); print()  # A B D C E G H F 
postorderTraverse(root); print() # D B G H E C F A 

print("Copy /")
deepcopy = copyTree(root) # root not referenced
deepcopy['children'].append({'data': 'X', 'children': []})
preorderTraverse(deepcopy); print() # A B D C E G H F X
preorderTraverse(root); print()     # A B D C E G H F

print("Delete /")
copy = root # root is referenced
delTree(copy, 'C')
delTree(copy, 'F')
preorderTraverse(copy); print() # A B D
preorderTraverse(root); print() # A B D

assert root != deepcopy
assert root == copy