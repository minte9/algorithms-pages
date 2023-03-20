""" Evaluate board intermediate state
"""

import copy, sys

def get_legal_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
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

def show(board):
    for i in range(3):
        print(" ", board[i][0], "|", board[i][1], "|", board[i][2])
        print(" ---+---+---") if i < 2 else ""

def minimax(board, player=True, move=None):
    if is_terminal_state(board):
        return evaluate_score(board), move

    s = float("-inf") if player else float("+inf")
    for move in get_legal_moves(board):

        i, j = move
        new_board = copy.deepcopy(board)
        new_board[i][j] = 'X' if player else 'O'
        score_, move_ = minimax(new_board, not player, move)

        if is_terminal_state(new_board):
            return evaluate_score(new_board), move

        if player:
            s = max(score_, s)
            if (s > score_): move = move_
        else:
            s = min(score_, s)
            if (s < score_): move = move_

    return s, move


def play(board, player=True):

    score, move = minimax(board, player)
    i, j = move

    board[i][j] = 'X' if player else 'O'
    print("X" if player else "O", "move")
    show(board)

    if is_terminal_state(board):
        if evaluate_score(board) != 0:
            print(('X' if player else 'O'), 'won! \n')
        else:
            print('Draw!')
        return False

    play(board, not player)

print("\n-----------------------------")
board = [
    ["X", " ", "O"],
    ["O", "O", "X"],
    [" ", "X", " "],
]
print("X to move")
show(board)
play(board, True)

print("\n-----------------------------")
board = [
    ["X", " ", " "],
    ["X", "O", "X"],
    ["O", " ", "O"],
]
print("X to move")
show(board)
play(board, True)

print("\n-----------------------------")
board = [
    ["X", " ", " "],
    [" ", " ", " "],
    ["O", "X", "O"],
]
print("X to move")
show(board)
play(board, True)