# Game - 2 - Tic Tac Toe with numbers - By Sohaila Abdelazim Khalifa - 20210492. 

# to avoid an error of conting the defult zero in the array as a number and satsfying the condtion of winning. 
# did an background array to work on with a high number. 
cells_background = [ [ 100 , 100 , 100 ], [100 , 100 , 100 ], [100 , 100 , 100] ]

# function to display the  game board on screen to user.
# using numby libarary to make a multidimensional array. 
import numpy as np 
cells_numbers = [ [ 0 , 0 , 0 ], [0 , 0 , 0 ], [0 , 0 , 0] ]
def display_game_board():
  for row in cells_numbers: 
    print(*row , sep = " ")

# checking the cells avaiblity.
vaild_cells = [[ False, False , False], [False , False , False ], [ False , False , False ]]

# player 1 function to input the numbers and choose the cell to enter it. 
player1_numbers = [ 1, 3 , 5 , 7 , 9 ]
def player_1(player):
  input_cells_row = int(input ( player + "please enter the index of cell row (0 , 1 , 2 ):"))
  input_cells_coulmn = int(input (player + "please enter the index of cell column (0 , 1 , 2 ) : "))
  number_input = int(input (  player + "please enter the number :  "))
  # defensive to enter only odd numbers btween 0 to 9 
  while number_input not in player1_numbers : 
    number_input = int(input (" please enter only other odd numbers : "))
  # defensive to not chosse the same cell twice.  
  while (input_cells_row < 0 or input_cells_coulmn < 0 or input_cells_row >3 or input_cells_coulmn >3
        or vaild_cells[input_cells_row-1][input_cells_coulmn-1]==True):
    input_cells_row = int(input ("please enter another cell row number  :  "))
    input_cells_coulmn = int(input ("please enter another cell column number  :  "))
  # change the status after choosing the cell by the player. 
  vaild_cells[input_cells_row-1][input_cells_coulmn-1] = True 
  # update_displayarray 
  cells_numbers[input_cells_row][input_cells_coulmn] = number_input
  #update_backgroundarray 
  cells_background[input_cells_row][input_cells_coulmn] = number_input
  # As the player can use the number only once. 
  player1_numbers.remove(number_input) 
  print( player1_numbers)
  
# player 2 function to input the numbers and choose the cell to enter it. 
player2_numbers = [ 0, 2 , 4 , 6 , 8 ]
def player_2(player):
  input_cells_row = int(input ( player + "please enter the index of cell row (0 , 1 , 2 ) : "))
  input_cells_coulmn = int(input (player + "please enter the index of cell column (0 , 1 , 2 ) : "))
  number_input = int(input ( player +"please enter the number  :  "))
  while number_input not in player2_numbers : 
    number_input = int(input (" please enter only other even numbers : "))
  while (input_cells_row < 0 or input_cells_coulmn < 0 or input_cells_row >3 or input_cells_coulmn >3
        or vaild_cells[input_cells_row-1][input_cells_coulmn-1]==True):
    input_cells_row = int(input ("please enter another cell row number  :  "))
    input_cells_coulmn = int(input ("please enter another cell column number  :  "))

  vaild_cells[input_cells_row-1][input_cells_coulmn-1] = True 
  cells_numbers[input_cells_row][input_cells_coulmn] = number_input
  cells_background[input_cells_row][input_cells_coulmn] = number_input
  player2_numbers.remove(number_input) 
  print(player2_numbers)

# cases which makes the player win. 
winner = False 
def winner_player():
  global winner
  if   ((cells_background[0][0]) + (cells_background[0][1]) + (cells_background[0][2]) ) == 15 :   # rows cases
   winner = True  
  elif ((cells_background[1][0]) + (cells_background[1][1]) + (cells_background[1][2]) ) == 15 :
   winner = True  
  elif ((cells_background[2][0]) + (cells_background[2][1]) + (cells_background[2][2]) ) == 15 :
   winner = True  
  elif ((cells_background[0][0]) + (cells_background[1][0]) + (cells_background[2][0]) ) == 15 :   # columns cases
   winner = True  
  elif ((cells_background[1][0]) + (cells_background[1][1]) + (cells_background[1][2]) ) == 15 :
   winner = True  
  elif ((cells_background[2][0]) + (cells_background[2][1]) + (cells_background[2][2]) ) == 15 :
   winner = True  
  elif ((cells_background[0][0]) + (cells_background[1][1]) + (cells_background[2][2]) ) == 15 :   # cross cases
   winner = True  
  elif ((cells_background[0][2]) + (cells_background[1][1]) + (cells_background[2][0]) ) == 15 :
   winner = True  
  else : 
    winner = False 
  return winner 
# calling the playing function. 
def play_game():  
  global winner 
  display_game_board()
  n_actions = 9
  while (n_actions > 0 ):

    player_movement = player_1 (' player 1 ')
    winner_player()
    display_game_board()
    if (winner == True):
      print ('player 1 wins')
      break
    n_actions -= 1

    if (n_actions == 0):
      break

    player_movement = player_2(' player 2 ')
    winner_player()
    display_game_board()
    if (winner == True):
      print ('player 2 wins')
      break
    n_actions -= 1

  if (n_actions == 0 and winner == False):
    print ('End of game - Draw')
play_game()