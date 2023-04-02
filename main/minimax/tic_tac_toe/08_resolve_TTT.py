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
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return 1 if board[i][0] == 'X' else -1 # horizontal win score
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return 1 if board[0][i] == 'X' else -1 # vertical win score

    if (board[0][0] == board[1][1] == board[2][2] or \
        board[0][2] == board[1][1] == board[2][0]) and board[1][1] != " ":
            return 1 if board[1][1] == "X" else -1 # diagonal win score 
    return 0

def is_terminal_state(board):
    if (evaluate_score(board)) ==  1:    return True # X win
    if (evaluate_score(board)) == -1:    return True # O win
    if len(get_legal_moves(board)) == 0: return True # Draw
    return False

def show(board, move=None):
    board_ = np.copy(board).tolist() # color move
    if move: 
        i, j = move
        board_[i][j] = '\033[96m' + board[move] + '\033[0m'

    for i in range(3):
        print(" ", board_[i][0], "|", board_[i][1], "|", board_[i][2])
        print(" ---+---+---") if i < 2 else ""


def minimax(board, player=True):
    v = float("-inf") if player else float("+inf")
    for move in get_legal_moves(board): 
        
        new_board = np.copy(board)
        new_board[move] = 'X' if player else 'O'

        if is_terminal_state(new_board):  # Base case
            return move, evaluate_score(new_board)

        move, score = minimax(new_board, not player) # Recursive case

        if score == 1 or score == -1: # Prunning (win move)
            break
        
        if player:
            v = max(score, v)
        else:
            v = min(score, v) 

    return move, v


def play(board, player=True, expected=None):
    print("\nX" if player else "\nO", "move")

    best_move, s = minimax(board, player)
    board[best_move] = 'X' if player else 'O'
    show(board, best_move)
    score = evaluate_score(board)

    if is_terminal_state(board):
        assert expected == score
        if score ==  1: print('X won! \n')
        if score == -1: print('O won! \n')
        if score ==  0: print('Draw!  \n')
        return False

    play(board, not player, expected) # Recursive case

games = [
    (
        np.array([
            ["X", " ", " "],
            ["X", "O", " "],
            ["O", " ", " "],]), True, 0
    ), (
        np.array([
            ["X", "O", "X"],
            ["O", "X", " "],
            ["O", "X", " "],]), False, 0
    ), (
        np.array([
            [" ", "O", "X"],
            ["O", "X", " "],
            [" ", "X", " "],]), False, 0
    ), (
        np.array([
            ["X", "O", " "],
            ["X", "X", "O"],
            ["O", " ", " "],]), True, 1
    ), (
        np.array([
            ["X", "O", "X"],
            ["X", " ", " "],
            ["O", " ", "O"],]), True, 0
    ), (
        np.array([
            ["X", "O", " "],
            [" ", " ", " "],
            [" ", " ", " "],]), True, 1
    ), (
        np.array([
            ["X", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],]), False, 0
    ), (
        np.array([
            [" ", " ", " "],
            [" ", "X", " "],
            [" ", " ", " "],]), False, 1
    ), (
        np.array([
            ["0", " ", "X"],
            [" ", "X", " "],
            ["O", " ", " "],]), True, 0
    ),
    # (
    #     np.array([
    #         ["0", " ", " "],
    #         [" ", "X", " "],
    #         [" ", " ", " "],
    #     ]), True, 0
    # ),
]

for board, player, expected in games:
    print("-----------------------------")
    print('X' if player else 'O', 'to move')
    show(board)
    play(board, player, expected)