""" Given a grid 4x3, find the maximum connected colors

https://www.youtube.com/watch?v=IWvbPIYQPFM
"""

grid = [
    [0, 0, 1, 2],
    [0, 1, 2, 1],
    [2, 1, 1, 1],
]

UP, DOWN, LEFT, RIGHT = 'up', 'down', 'left', 'right'

def get_max_connected(y, x, parent=None):

    if x < 0 or y < 0 or x == len(grid[0]) or y == len(grid): # Base case
        return 0
    
    max = 0
    curr_item = grid[y][x]

    # Up
    if y-1 > 0:
        if curr_item == grid[y-1][x] and parent != DOWN: 
            max += 1 + get_max_connected(y-1, x, UP) # Recursive    

    # Down
    if y+1 < len(grid):
        if curr_item == grid[y+1][x] and parent != UP: 
            max += 1 + get_max_connected(y+1, x, DOWN)

    # Left
    if x-1 > 0:
        if curr_item == grid[y][x-1] and parent != RIGHT: 
            max += 1 + get_max_connected(y, x-1, LEFT)

    # Right
    if x+1 < len(grid[0]):
        if curr_item == grid[y][x+1] and parent != LEFT: 
            max += 1 + get_max_connected(y, x+1, RIGHT)

    return max
    
totals = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        max_ = get_max_connected(y, x)
        totals.append(max_)

print(totals)
    # [2, 0, 0, 0, 0, 4, 0, 4, 0, 4, 4, 4]

print("Maxim connected:", max(totals) + 1)  # 1 for item itself
    # 5