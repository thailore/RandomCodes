from connect_four import *

def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      #The "X" player finds their best move.
      result = minimax(my_board, True, 4, -float("Inf"), float("Inf"), my_evaluate_board)
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        #The "O" player finds their best move
        result = minimax(my_board, False, 4, -float("Inf"), float("Inf"), codecademy_evaluate_board)
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")

def my_evaluate_board(board):
  # if game is over
  if has_won(board, "X"):
    return float("Inf")
  elif has_won(board, "O"):
    return -float("Inf")
  x_streak, o_streak = 0, 0
  
  for col in range(len(board) - 1):
    for row in range(len(board[0])):
      if board[col][row] and board[col+1][row] == 'X' and enough_space_to_win(len(board[0]), row, 2):
        x_streak += 1
      if board[col][row] and board[col+1][row] == 'O' and enough_space_to_win(len(board[0]), row, 2):
        o_streak += 1
      
  return x_streak - o_streak
  
def enough_space_to_win(length_of_row, current_index, current_streak):
  return (current_index + 4 - current_streak) <= (length_of_row - 1)

two_ai_game()
