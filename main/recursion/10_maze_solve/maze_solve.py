""" Maze solve
S marks the start, E the end of the maze.
The maze cannot have loops, otherwise the algorithm will not work.

The recursive case when the tree traversal algorithm moves 
from one node to next. When it reaches a dead end (a base case), 
it must backtrack to an earlier node to follow a different path.
"""

MAZE = """
#######################################################################
#S#                 #       # #   #     #         #     #   #         #
# ##### ######### # ### ### # # # # ### # # ##### # ### # # ##### # ###
# #   #     #     #     #   # # #   # #   # #       # # # #     # #   #
# # # ##### # ########### ### # ##### ##### ######### # # ##### ### # #
#   #     # # #     #   #   #   #         #       #   #   #   #   # # #
######### # # # ##### # ### # ########### ####### # # ##### ##### ### #
#       # # # #     # #     # #   #   #   #     # # #   #         #   #
# # ##### # # ### # # ####### # # # # # # # ##### ### ### ######### # #
# # #   # # #   # # #     #     #   #   #   #   #   #     #         # #
### # # # # ### # # ##### ####### ########### # ### # ##### ##### ### #
#   # #   # #   # #     #   #     #       #   #     # #     #     #   #
# ### ####### ##### ### ### ####### ##### # ######## ### ### ##### ###
#   #         #     #     #       #   # #   # #     #   # #   # #   # #
### ########### # ####### ####### ### # ##### # # ##### # # ### # ### #
#   #   #       # #     #   #   #     #       # # #     # # #   # #   #
# ### # # ####### # ### ##### # ####### ### ### # # ####### # # # ### #
#     #         #     #       #           #     #           # #      E#
#######################################################################
""".split('\n')

# Constants
EMTPY = ' '
START = 'S'
EXIT = 'E'
PATH = '\033[92m' + '0' + '\033[0m'

# Set WIDTH to the widest row's width
HEIGHT = len(MAZE)
WIDTH = 0
for row in MAZE: 
    if len(row) > WIDTH: 
        WIDTH = len(row)

# Matrix, make each row a list as wide as WIDTH
for i in range(HEIGHT):
    MAZE[i] = list(MAZE[i])
    if len(MAZE[i]) != WIDTH:       # first and last elements in list are []
        MAZE[i] = [EMTPY] * WIDTH   # make them blank rows

def printMaze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(MAZE[y][x], end='')
        print()

def findStart(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if maze[y][x] == START:
                return y, x

def solveMaze(maze, y=None, x=None, visited=[]):
    if x == None and y == None:
        y, x = findStart(maze)
        maze[y][x] = EMTPY # Get rid of 'S' from the maze

    if maze[y][x] == EXIT: # Base case
        printMaze(maze)
        return True

    maze[y][x] = PATH # Mark the path progression
    visited.append(str(y) + ',' + str(x))
    # printMaze(maze) # Uncoment to view each step

    # North
    if y + 1 < HEIGHT:
        seen = str(y + 1) + "," + str(x) in visited
        open = maze[y + 1][x] in (EMTPY, EXIT)
        if open and not seen:
            if solveMaze(maze, y + 1, x, visited): # Recursive case
                return True

    # South
    if y - 1 >= 0:
        seen = str(y - 1) + "," + str(x) in visited
        open = maze[y - 1][x] in (EMTPY, EXIT)
        if open and not seen:
            if solveMaze(maze, y - 1, x, visited): # Recursive case
                return True

    # Est
    if x + 1 < WIDTH:
        seen = str(y) + "," + str(x + 1) in visited
        open = maze[y][x + 1] in (EMTPY, EXIT)
        if open and not seen:
            if solveMaze(maze, y, x + 1, visited): # Recursive case
                return True

    # West
    if x - 1 >= 0:
        seen = str(y) + "," + str(x - 1) in visited
        open = maze[y][x - 1] in (EMTPY, EXIT)
        if open and not seen:
            if solveMaze(maze, y, x - 1, visited): # Recursive case
                return True 

    # Backtrac step
    maze[y][x] = EMTPY

    return False

    
printMaze(MAZE)
solveMaze(MAZE) # The list MAZE is modified in place 
printMaze(MAZE) # Python pass a reference to the list, not a copy

"""
#######################################################################
#0#                 #       # #   #     #         #     #   #         #
#0##### ######### # ### ### # # # # ### # # ##### # ### # # ##### # ###
#0#000#     #     #     #   # # #   # #   # #       # # # #     # #   #
#0#0#0##### # ########### ### # ##### ##### ######### # # ##### ### # #
#000#00000# # #     #   #   #   #         #       #   #   #   #   # # #
#########0# # # ##### # ### # ########### ####### # # ##### ##### ### #
#       #0# # #     # #     # #   #   #   #     # # #   #         #000#
# # #####0# # ### # # ####### # # # # # # # ##### ### ### #########0#0#
# # #   #0# #   # # #     #     #   #   #   #   #   #     #      000#0#
### # # #0# ### # # ##### ####### ########### # ### # ##### #####0###0#
#   # #  0# #00 # #     #   #     #    00 #00 #00   # #0000 #00  0#  0#
         000000000                     0000000 00      000000000 0   0 
#   #    0000 #000  #     #       #   #0#00 #0#000  #  0# #00 #0#0  #0#
### ########### #0####### ####### ### #0#####0#0#0#####0# # ###0#0###0#
#   #   #       #0#00000#   #000#     #0   000#0#0#00000# # #  0#0#  0#
# ### # # #######0#0###0#####0#0#######0###0###0#0#0####### # #0#0###0#
#     #         #000  #0000000#000000000  #00000#000        # #000   E#
#######################################################################
"""
