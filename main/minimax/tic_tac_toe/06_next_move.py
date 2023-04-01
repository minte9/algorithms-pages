""" Tic Tac Toe
Evaluate board intermediate state
"""

import copy

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
    
    for i in range(3): # horizonal win
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return True

    for i in range(3): # vertical win
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return True

    # diagonal win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ": return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ": return True

    for i in range(3): # draw
        for j in range(3):
            if board[i][j] == " ": return False

    return True

def show(board):
    for i in range(3):
        print(" ", board[i][0], "|", board[i][1], "|", board[i][2])
        print(" ---+---+---") if i < 2 else ""

def play(board, player=True, debug=True):

    legal_moves = get_legal_moves(board)
    scores = []
    
    for (i, j) in legal_moves:
        board[i][j] = 'X' if player else 'O'
        s = evaluate_score(board)
        scores.append(s)
        board[i][j] = ' ' # reset

    minmax = max(scores) if player else min(scores)
    key = scores.index(minmax)
    move = legal_moves[key]

    if debug:
        print("Legal moves:", legal_moves) # [(0, 1), (1, 2), (2, 1)]
        print("Moves scores:", scores) # [1, 0, 0]
        print("Move:", move, "Score:", minmax) # (0, 1)

    print("\n", "X" if player else "O", 'move')
    i, j = move
    board[i][j] = 'X' if player else 'O'

    show(board)

    if is_terminal_state(board):
        print(('X' if player else 'O'), 'won! \n')
        return False

    play(board, not player)

print("-----------------------------")
board = [
    ["X", " ", " "],
    ["X", "O", " "],
    ["O", " ", " "],
]
print("X to move")
show(board)
play(board, True)
print("-----------------------------")

board = [
    ["X", "O", "X"],
    ["X", " ", " "],
    ["O", " ", "O"],
]
print("\nX to move")
show(board)
play(board, True)
print("-----------------------------")