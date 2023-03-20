""" Evaluate board intermediate state
"""

def get_legal_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

def evaluate_score(board):

    for i in range(3): # horizontal win score
        if board[i][0] == board[i][1] == board[i][2]:
            return 1 if board[i][0] == 'X' else -1

    for i in range(3): # vertical win score
        if board[0][i] == board[1][i] == board[2][i]:
            return 1 if board[0][i] == 'X' else -1

    # diagonal win score
    if board[0][0] == board[1][1] == board[2][2] or \
       board[0][2] == board[1][1] == board[2][0]:
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


board = [
    ["X", " ", "X"],
    ["X", "O", " "],
    ["O", " ", "O"],
]

# Get legal moves
legal_moves = get_legal_moves(board)
print("Legal moves:", legal_moves) # [(0, 1), (1, 2), (2, 1)]

# Evaluate score (X move)
players_scores = []
for player in [True, False]:

    scores = []
    for (i, j) in legal_moves:
        board[i][j] = 'X' if player else 'O'
        s = evaluate_score(board)
        scores.append(s)
        board[i][j] = ' ' # reset

    players_scores.append(scores)
print("Players' scores", players_scores) # [[1, 0, 0], [0, 0, -1]]

# Check terminal state
terminal_states = []
for player in [True, False]:

    states = []
    for (i, j) in legal_moves:
        board[i][j] = 'X' if player else 'O'
        t = is_terminal_state(board)
        states.append(t)
        board[i][j] = ' ' # reset

    terminal_states.append(states)
print("Terminal states:", terminal_states) # [[True, False, False], [False, False, True]]