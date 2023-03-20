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


def minimax(board, player=True, best_move=None, alpha=float("-inf"), beta=float("+inf"), depth=0, mindepth=0):

    debug = True

    # initialize best score
    best_score = float("-inf") if player else float("+inf")
    for move in get_legal_moves(board):

        if debug:
            if depth == 1: print("----------------")

        if best_move == None: best_move = move

        new_board = np.copy(board)
        new_board[move] = 'X' if player else 'O'

        s = evaluate_score(new_board)

        if player:
            if (s >= best_score and depth <= mindepth): 
                best_move = move
            best_score = max(s, best_score)
            alpha = max(alpha, best_score) 
        else:
            if (s <= best_score and depth <= mindepth): 
                best_move = move
            best_score = min(s, best_score)
            beta = min(beta, best_score)

        if debug:
            print(' ' * depth, 'X' if player else 'O', 'turn', best_move, best_score)

        if (beta < alpha): 
            if debug:
                print(' ' * depth, '   ', f'b/ beta:{beta} < alpha:{alpha}', "depth:", depth, "\033[96m", best_move, best_score, '\033[0m')
            return best_score, best_move

        if is_terminal_state(new_board):
            if debug:
                print(' ' * depth, '   ', f't/ beta:{beta} < alpha:{alpha}', "depth:", depth, "\033[96m", best_move, best_score, '\033[0m')
            return best_score, best_move
        
        if debug:
            print(' ' * depth, '   ', f'n/ beta:{beta} < alpha:{alpha}', "depth:", depth, "\033[96m", best_move, best_score, '\033[0m')
            
        best_score, best_move = minimax(new_board, not player, best_move, alpha, beta, depth, mindepth) # recursive
        
        depth = depth + 1
        mindepth = min(mindepth, depth)

    return best_score, best_move


def play(board, player=True):
    
    score, move = minimax(board, player)
    board[move] = 'X' if player else 'O'

    print("\n", "X" if player else "O", "move")
    show(board, move)
    print()

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
    ["X", "O", " "],
    ["O", "X", " "],
    [" ", "X", " "],
])
print("O to move")
show(board)
play(board, False)

sys.exit()





sys.exit()

# print("\n-----------------------------")
board = np.array([
    ["X", "O", " "],
    [" ", " ", " "],
    [" ", " ", " "],
])
print("X to move")
show(board)
play(board, True)
print("Iterations:", i)

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