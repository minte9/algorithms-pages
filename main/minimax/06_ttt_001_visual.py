""" Tic Tac Toe - Visual representation
"""

import numpy as np
import pandas as pd

def show_board(msg, matrix, header=['']):
    board = pd.DataFrame(matrix)
    board.columns = header
    board = board.to_markdown(index=False)
    print(msg)
    print(board, "\n")

print("--------------------------------------")
matrix = [
    ['X O X'],
    ['X    '],
    ['O   O']]
options = [
    ['X O X', 'X O X', 'X O X'],
    ['X X  ', 'X   X', 'X    '],
    ['O   O', 'O   O', 'O X O']]
move = [
    ['X O X'],
    ['X X  '],
    ['O   O']]
show_board('X to move', matrix)
show_board('X options', options, header=[-1, -1, 0])
show_board('X move', move)

print("--------------------------------------")
matrix = [
    ['X O X'],
    ['X X  '],
    ['O   O']]
options = [
    ['X O X', 'X O X'],
    ['X X  ', 'X X O'],
    ['O O O', 'O   O']]
move1 = [
    ['X O X'],
    ['X X  '],
    ['O O O']]
move2 = [
    ['X O X'],
    ['X X O'],
    ['O   O']]
show_board('O to move', matrix)
show_board('O options', options, header=[-1, 0])
show_board('O move (wins)', move1, header=[-1])
show_board('O move (draw)', move2, header=[0])


"""
--------------------------------------
X to move
|       |
|:------|
| X O X |
| X     |
| O   O |

X options
| -1    | -1    | 0     |
|:------|:------|:------|
| X O X | X O X | X O X |
| X X   | X   X | X     |
| O   O | O   O | O X O |

X move
|       |
|:------|
| X O X |
| X X   |
| O   O |

--------------------------------------
O to move
|       |
|:------|
| X O X |
| X X   |
| O   O |

O options
| -1    | 0     |
|:------|:------|
| X O X | X O X |
| X X   | X X O |
| O O O | O   O |

O move (wins)
| -1    |
|:------|
| X O X |
| X X   |
| O O O |

O move (draw)
| 0     |
|:------|
| X O X |
| X X O |
| O   O |
"""