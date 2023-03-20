""" Minimax algorithm
Color last move, dictionary refactoring
"""

import sys
import numpy as np

def get_legal_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i, j] == " ":
                moves.append((i, j))
    return moves

def evaluate_score(board):

    # horizontal win score
    for i in range(3): 
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return 1 if board[i][0] == 'X' else -1

    # vertical win score
    for i in range(3): 
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return 1 if board[0][i] == 'X' else -1

    # diagonal win score
    if (board[0][0] == board[1][1] == board[2][2] or \
        board[0][2] == board[1][1] == board[2][0]) and board[1][1] != " ":
            return 1 if board[1][1] == "X" else -1

    return 0

def is_terminal_state(board):
    if (evaluate_score(board)) ==  1:    return True # X win
    if (evaluate_score(board)) == -1:    return True # O win
    if len(get_legal_moves(board)) == 0: return True # Draw
    return False

def show(board, move=None):

    # color move
    board_ = np.copy(board).tolist()
    if move: 
        i, j = move
        board_[i][j] = '\033[96m' + board[move] + '\033[0m'

    # show current board
    for i in range(3):
        print(" ", board_[i][0], "|", board_[i][1], "|", board_[i][2])
        print(" ---+---+---") if i < 2 else ""


def minimax(board, player=True, i=0):

    debug = True
    i = i + 1
    v = float("-inf") if player else float("+inf")

    if debug:
        if i == 1: 
            print("------------------------------")


    for move in get_legal_moves(board): 

        # if i == 1: print(' ' * i, "legal_moves:", get_legal_moves(board))

        new_board = np.copy(board)
        new_board[move] = 'X' if player else 'O'
        
        s = evaluate_score(new_board)

        if player:
            v = max(s, v)
        else:
            v = min(s, v)           

        if debug:
            print(' ' * i, f"\033[96mX\033[0m" if player else 'O', 'turn', move, \
                f"\033[96m{v}\033[0m" if is_terminal_state(new_board) else "")

        if is_terminal_state(new_board):
            return v, move
        
        if v == 1 or v == -1: 
            return v, move

        v, move = minimax(new_board, not player, i) # recursive

    return v, move


def play(board, player=True):

    s, m = minimax(board, player)
    best_move = m

    print("\n", "X" if player else "O", "move")
    board[best_move] = 'X' if player else 'O'
    show(board, best_move)

    if is_terminal_state(board):
        if evaluate_score(board) != 0:
            print(('X' if player else 'O'), 'won! \n')
        else:
            print('Draw! \n')
        return False

    play(board, not player)

# print("-----------------------------")
# board = np.array([
#     ["X", " ", " "],
#     ["X", "O", " "],
#     ["O", " ", " "],
# ])
# print("X to move")
# show(board)
# play(board, True)

# sys.exit()

print("\n-----------------------------")
board = np.array([
    ["X", "O", "X"],
    ["O", "X", " "],
    ["O", "X", " "],
])
print("O to move")
show(board)
play(board, False)

sys.exit()

print("\n-----------------------------")
board = np.array([
    ["X", "O", "X"],
    ["O", "X", " "],
    ["O", "X", " "],
])
print("O to move")
show(board)
play(board, False)

sys.exit()

print("\n-----------------------------")
board = np.array([
    [" ", "O", "X"],
    ["O", "X", " "],
    [" ", "X", " "],
])
print("O to move")
show(board)
play(board, False)

sys.exit()

# print("\n-----------------------------")
board = np.array([
    ["X", "O", " "],
    ["X", "X", "O"],
    ["O", " ", " "],
])
print("X to move")
show(board)
play(board, True)

sys.exit()

board = np.array([
    ["X", "O", "X"],
    ["X", " ", " "],
    ["O", " ", "O"],
])
print("\nX to move")
show(board)
play(board, True)
print("-----------------------------")