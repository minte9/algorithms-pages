""" Tic Tac Toe
Get available legal moves
"""

# Game start
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

# X move
board = [
    ["-", "-", "-"],
    ["-", "X", "-"],
    ["-", "-", "-"],
]

def get_legal_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                moves.append((i, j))
    return moves

print(get_legal_moves(board))
    # (0, 0) (0, 1) (0, 2)
    # (1, 0)        (1, 2) 
    # (2, 0) (2, 1) (2, 2)
