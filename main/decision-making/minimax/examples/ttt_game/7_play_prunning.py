""" Minimax algorithm
Color last move, dictionary refactoring
"""

import copy, sys
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
    if (evaluate_score(board)) ==  1: return True # X win
    if (evaluate_score(board)) == -1: return True # O win
    if len(get_legal_moves(board)) == 0:
        return True 
    return False

def show(board, move=None):

    board_ = np.copy(board).tolist()
    if move: 
        i, j = move
        board_[i][j] = '\033[96m' + board[move] + '\033[0m'

    for i in range(3):
        print(" ", board_[i][0], "|", board_[i][1], "|", board_[i][2])
        print(" ---+---+---") if i < 2 else ""


def minimax(board, player=True, move=None):
    global iterations

    if is_terminal_state(board):
        return evaluate_score(board), move

    # initialize score
    s = float("-inf") if player else float("+inf")
    for move in get_legal_moves(board):

        new_board = copy.deepcopy(board)
        new_board[move] = 'X' if player else 'O'

        # recursively evaluate children boards
        score_, move_ = minimax(new_board, not player, move)
        iterations = iterations + 1

        if player:
            s = max(score_, s)
            if (s > score_): move = move_
        else:
            s = min(score_, s)
            if (s < score_): move = move_

        if is_terminal_state(new_board):
            return evaluate_score(new_board), move
            
    return s, move


def play(board, player=True):

    score, move = minimax(board, player)
    board[move] = 'X' if player else 'O'
    

    print("\n", "X" if player else "O", "move")
    show(board, move)

    if is_terminal_state(board):
        if evaluate_score(board) != 0:
            print(('X' if player else 'O'), 'won! \n')
        else:
            print('Draw!')
        return False

    play(board, not player)


iterations = 0

print("\n-----------------------------")
board = np.array([
    ["X", "O", " "],
    [" ", " ", " "],
    [" ", " ", " "],
])
print("X to move")
show(board)
play(board, True)

print("-----------------------------")
board = np.array([
    ["X", " ", " "],
    ["X", "O", " "],
    ["O", " ", " "],
])
print("X to move")
show(board)
play(board, True)
print("-----------------------------")

board = np.array([
    ["X", "O", "X"],
    ["X", " ", " "],
    ["O", " ", "O"],
])
print("\nX to move")
show(board)
play(board, True)
print("-----------------------------")