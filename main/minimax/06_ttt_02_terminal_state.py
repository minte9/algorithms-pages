""" Tic Tac Toe
Check for terminal state
"""

def is_terminal_state(board):

    # Check for horizontal win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return True

    # Check for vertical win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return True

    # Check for diagonal win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ": return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ": return True

    # Check for draw
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ": return False

    return True


board = [
    ["X", "O", "X"],
    ["X", " ", "X"],
    ["O", " ", "O"],
]
board[1][1] = 'X'; assert is_terminal_state(board) == True # horizontal win
board[1][1] = 'O'; assert is_terminal_state(board) == False

board = [
    ["X", "O", "X"],
    ["X", " ", "X"],
    ["O", "O", " "],
]
board[2][2] = 'X'; assert is_terminal_state(board) == True # vertical win
board[2][2] = 'O'; assert is_terminal_state(board) == True

board = [
    ["X", "O", "O"],
    ["X", " ", " "],
    ["O", " ", "X"],
]
board[1][1] = 'X'; assert is_terminal_state(board) == True # diagonal win
board[1][1] = 'O'; assert is_terminal_state(board) == True

board = [
    ["X", "O", " "],
    ["O", " ", "X"],
    ["O", "X", "O"],
]
board[0][2] = 'X'; assert is_terminal_state(board) == False 
board[1][1] = 'O'; assert is_terminal_state(board) == True # draw
