root = {'name': 'A', 'children': []}
node2 = {'name': 'B', 'children': []}
node3 = {'name': 'C', 'children': []}
node4 = {'name': 'D', 'children': []}
node5 = {'name': 'E', 'children': []}
node6 = {'name': 'F', 'children': []}
node7 = {'name': 'G', 'children': []}
node8 = {'name': 'H', 'children': []}

root['children'] = [node2, node3]
node2['children'] = [node4]
node3['children'] = [node5, node6]
node5['children'] = [node7, node8]

print(node3['children'])

"""
[{'name': 'E', 'children': 
    [{'name': 'G', 'children': []}, 
     {'name': 'H', 'children': []}]}, 
 {'name': 'F', 'children': []}]
"""