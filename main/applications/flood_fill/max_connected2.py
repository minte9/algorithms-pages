""" Given a grid 4x3, find the maximum connected colors
Iterative solution

https://www.youtube.com/watch?v=IWvbPIYQPFM
"""

grid = [
    [0, 0, 1, 2],
    [0, 1, 2, 1],
    [2, 1, 1, 1],
]

connections = {'0': 1, '1': 1, '2': 1}

for y in range(len(grid)):
    for x in range(len(grid[0])):

        v = grid[y][x] # current item value
            
        # Right
        if x+1 < len(grid[0]):
            if v == grid[y][x+1]: connections[str(v)] += 1

        # Down
        if y+1 < len(grid):
            if v == grid[y+1][x]: connections[str(v)] += 1

print(connections) 
    # {'0': 3, '1': 5, '2': 1}

print(max(connections.values()))
    # 5