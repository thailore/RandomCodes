from tic_tac_toe import *
from copy import deepcopy

def game_is_over(board):
  return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0

def evaluate_board(board):
  if has_won(board, "X"):
    return 1
  elif has_won(board, "O"):
    return -1
  else:
    return 0

def minimax(input_board, is_maximizing):
  # Base case - the game is over, so we return the value of the board
  if game_is_over(input_board):
    return [evaluate_board(input_board), ""]
  # The maximizing player
  if is_maximizing:
    # The best value starts at the lowest possible value
    best_value = -float("Inf")
    best_move = ""
    # Loop through all the available moves
    for move in available_moves(input_board):
      # Make a copy of the board and apply the move to it
      new_board = deepcopy(input_board)
      select_space(new_board, move, "X")
      # Recursively find your opponent's best move
      hypothetical_value = minimax(new_board, False)[0]
      # Update best value if you found a better hypothetical value
      if hypothetical_value > best_value:
        best_value = hypothetical_value
        best_move = move
    return [best_value, best_move]
  # The minimizing player
  else:
    # The best value starts at the highest possible value
    best_value = float("Inf")
    best_move = ""
    # Testing all potential moves
    for move in available_moves(input_board):
      # Copying the board and making the move
      new_board = deepcopy(input_board)
      select_space(new_board, move, "O")
      # Passing the new board back to the maximizing player
      hypothetical_value = minimax(new_board, True)[0]
      # Keeping track of the best value seen so far
      if hypothetical_value < best_value:
        best_value = hypothetical_value
        best_move = move
    return [best_value, best_move]
