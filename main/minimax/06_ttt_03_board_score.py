""" Tic Tac Toe
Check for terminal state
"""

def score(board):

    # score for horizontal win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return 1 if board[i][0] == 'X' else -1

    # score for vertical win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return 1 if board[0][i] == 'X' else -1

    # score for diagonal win
    if board[0][0] == board[1][1] == board[2][2] or \
       board[0][2] == board[1][1] == board[2][0]:
       return 1 if board[1][1] == "X" else -1

    return 0


board = [
    ["X", " ", "X"],
    ["X", "O", " "],
    ["O", " ", "O"],
]
board[0][1] = 'X'; assert score(board) == 1 # horizontal win (X)
board[0][1] = ' '; 
board[2][1] = 'O'; assert score(board) == -1  # horizontal win (O)

board = [
    ["X", "X", " "],
    ["X", "O", "O"],
    [" ", " ", "O"],
]
board[2][0] = 'X'; assert score(board) == 1 # vertical win (X)
board[2][0] = ' '; 
board[0][2] = 'O'; assert score(board) == -1 # vertical win (O)

board = [
    ["X", "X", "O"],
    ["X", " ", " "],
    ["O", " ", "X"],
]
board[1][1] = 'X'; assert score(board) == 1 # vertical win (X)
board[1][1] = ' '; 
board[1][1] = 'O'; assert score(board) == -1 # vertical win (O)

board = [
    ["X", "0", "X"],
    ["X", " ", "O"],
    ["O", "X", "O"],
]
board[1][1] = 'X'; assert score(board) == 0 # draw
board[1][1] = ' '; 
board[1][1] = 'O'; assert score(board) == 0 # draw