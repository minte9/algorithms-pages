""" Example of using a queue for BFS 

Using set() for visited is more efficient than using a list
A set can perform 'in' test in constant time O(1).
A set enforces uniquness, it won't allow duplicates.
"""

from collections import deque
from icecream import ic

def bfs(graph, start_node):
    visited = set()
    queue = deque()

    queue.append(start_node)
    visited.add(start_node)

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            ic(neighbor)

            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'D'],
    'C': ['A', 'F'],
    'B': ['A', 'D', 'E'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'D': ['B'],
}

bfs(graph, 'A')

"""
    A
    ic| neighbor: 'B'
    ic| neighbor: 'D'
    B
    ic| neighbor: 'A'
    ic| neighbor: 'D'
    ic| neighbor: 'E'
    D
    ic| neighbor: 'B'
    E
    ic| neighbor: 'B'
    ic| neighbor: 'F'
    F
    ic| neighbor: 'C'
    ic| neighbor: 'E'
    C
    ic| neighbor: 'A'
    ic| neighbor: 'F'
"""