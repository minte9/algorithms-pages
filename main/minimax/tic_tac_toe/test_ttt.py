import random

# Define the game board and other necessary data structures
board = [' '] * 9
players = ['X', 'O']

# Define the legal_moves function
def legal_moves(board):
    return [i for i, x in enumerate(board) if x == ' ']

# Define the terminal_state function
def terminal_state(board):
    # Check if a player has won
    for player in players:
        for i in range(3):
            # Check rows
            if all(board[i*3 + j] == player for j in range(3)):
                return True
            # Check columns
            if all(board[i + j*3] == player for j in range(3)):
                return True
        # Check diagonals
        if all(board[i] == player for i in [0, 4, 8]) or all(board[i] == player for i in [2, 4, 6]):
            return True

    # Check if the board is full
    return all(x != ' ' for x in board)

# Define the evaluate function
def evaluate(board):
    # Check if a player has won
    for player in players:
        for i in range(3):
            # Check rows
            if all(board[i*3 + j] == player for j in range(3)):
                return 1 if player == 'X' else -1
            # Check columns
            if all(board[i + j*3] == player for j in range(3)):
                return 1 if player == 'X' else -1
        # Check diagonals
        if all(board[i] == player for i in [0, 4, 8]) or all(board[i] == player for i in [2, 4, 6]):
            return 1 if player == 'X' else -1

    # Check if the board is full
    if all(x != ' ' for x in board):
        return 0

    # If the game is not over, return None
    return None

# Define the minimax function
def minimax(board, depth, maximizing_player, alpha, beta):
    # Check if the current game state is a terminal state
    if terminal_state(board):
        return evaluate(board)

    # Check if the maximum depth has been reached
    if depth == 0:
        return evaluate(board)

    # If the current player is the maximizing player
    if maximizing_player:
        best_score = -float('inf')
        for move in legal_moves(board):
            new_board = board[:]
            new_board[move] = 'X'
            score = minimax(new_board, depth-1, False, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score

    # If the current player is the minimizing player
    else:
        best_score = float('inf')
        for move in legal_moves(board):
            new_board = board[:]
            new_board[move] = 'O'
            score = minimax(new_board, depth-1, True, alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

# Define the play function
def play():
    # Initialize the game state
    board = [' '] * 9
    player = 'X'
    depth = 9

    while True:
        print_board(board)

        # Check if the game is over
        if terminal_state(board):
            winner = evaluate(board)
            if winner == 1:
                print("X wins!")
            elif winner == -1:
                print("O wins!")
            else:
                print("Tie!")
            break

        # Get the current player's move
        if player == 'X':
            move = get_human_move(board)
        else:
            move = get_computer_move(board)

        # Make the move
        board[move] = player

        # Switch to the other player
        player = 'O' if player == 'X' else 'X'

        # Decrement the depth counter
        depth -= 1

        # Check if the maximum depth has been reached
        if depth == 0:
            print("Tie!")
            break

# Define the print_board function
def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

# Define the get_human_move function
def get_human_move(board):
    while True:
        move = input("Enter your move (0-8): ")
        if move.isdigit() and int(move) in legal_moves(board):
            return int(move)

# Define the get_computer_move function
def get_computer_move(board):
    best_move = None
    best_score = -float('inf')
    for move in legal_moves(board):
        new_board = board[:]
        new_board[move] = 'O'
        score = minimax(new_board, 8, True, -float('inf'), float('inf'))
        if score > best_score:
            best_move = move
            best_score = score
    return best_move



play()