""" Tic Tac Toe - Visual representation
"""

import numpy as np

def show(board):
    for i in range(3):
        print(" ", board[i][0], "|", board[i][1], "|", board[i][2])
        print(" ---+---+---") if i < 2 else ""

board = [
    ["X", "O", "X"],
    ["O", "X", " "],
    ["O", "X", " "],
]

show(board)