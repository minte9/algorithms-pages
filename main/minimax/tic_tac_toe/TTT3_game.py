""" Tic Tag Toe Game
"""

import numpy as np
import random, sys

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
    board_ = np.copy(board).tolist() 
    if move: 
        i, j = move
        CYAN, ENDC = '\033[96m', '\033[0m' # colored move
        board_[i][j] = CYAN + board[move] + ENDC 

    GRAY, ENDC = '\033[90m', '\033[0m' # colored numbers
    if 1 == 0: # activate colored numbers
        k = 0
        for i in range(3):
            for j in range(3):
                k = k + 1
                if board_[i][j] == " ": 
                    board_[i][j] = GRAY + str(k) + ENDC # colored number
                
    for i in range(3):
        print(" ", board_[i][0], "|", board_[i][1], "|", board_[i][2])
        print(" ---+---+---") if i < 2 else ""


# Minimax algorithm

def minimax(board, player=True, alpha=float('-inf'), beta=float('inf')):
    
    best_move = None 
    best_score = float("-inf") if player else float("+inf") # initialize score

    for move in get_legal_moves(board): # possible moves
        new_board = np.copy(board)
        new_board[move] = 'X' if player else 'O'
        
        if is_terminal_state(new_board): 
            return move, evaluate_score(new_board) # Base case

        # Recursive case
        move_, score_ = minimax(new_board, not player, alpha, beta)

        if player == True:
            if score_ > best_score:
                best_score = score_ # child best score
                best_move = move    # parent move
            alpha = max(alpha, score_)
            
        if player == False:
            if score_ < best_score:
                best_score = score_
                best_move = move
            beta = min(beta, score_)
        
        if beta <= alpha: # prunning condition
            break

    return best_move, best_score


# Game

def human_move(board):
    while True:
        n = input("\nEnter your move (1-9): ")
        
        if n.upper() == 'Q':
            sys.exit()

        if not n.isdigit(): 
            continue
        
        y = (int(n) - 1) // 3
        x = (int(n) - 1)  % 3
        if (y, x) in get_legal_moves(board): 
            return y, x

def start_board():
    return np.array([
            [" ", " ", " "], 
            [" ", " ", " "],
            [" ", " ", " "],
        ])

def game(board, player=True, total_score=0, X_score=0):    
    
    if player == True:
        move = human_move(board)
    
    if player == False:
        print("\nComputer move:")
        move, score = minimax(board, player)
        moves = get_legal_moves(board)

        # Variation: make the first computer move random (more interesting)
        if 1 == 1:
            if len(moves) == 8:
                move = random.choice(moves)

            # In this variation we need to prioritize the move that ends the game 
            # on next move (because we'll have multiple 'X' win moves)
            end = False
            for m in moves:
                new_board = np.copy(board); 
                new_board[m] = 'O'
                if is_terminal_state(new_board): 
                    move = m
                    end = True
                    break

            if end == False: # don't check for X if we already found an O end
                for m in moves:
                    new_board = np.copy(board); 
                    new_board[m] = 'X'
                    if is_terminal_state(new_board): 
                        move = m
                        break

    board[move] = 'X' if player else 'O'
    show(board, move)

    if is_terminal_state(board): # Base case
        score = evaluate_score(board)
        if score ==  1: print('\nX won!\n')
        if score == -1: print('\nO won!\n')
        if score ==  0: print('\nDraw!\n')

        if score == 1: 
            total_score += 1
            X_score     += 1 
        if score == 0: 
            total_score += 1
            X_score     += 0.5
        if score == -1: 
            total_score += 1
            X_score     += 0

        print("Your score: " + str(int(X_score * 100 / total_score)) + "% " + "\n")
        board = start_board() # reset
        show(board)
        player = False
                
    game(board, not player, total_score, X_score) # Recursive case



print("\nTic Tac Toe (random first computer move, Q to exit)\n")
board = start_board()
show(board)
game(board, True)