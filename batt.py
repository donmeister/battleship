#!/usr/bin/env python
# Battleship

from random import randint

# Functions

def print_board(board):
  print
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def hide_one_ship(ship):
    ship_size = ship_sizes[ship]
    ship_initial = ship_initials[ship]
#    print ship
#    print ship_size
#    print ship_initial
    empty = False
    while empty == False:
      hide_ship_row = random_row(ship_board)
      hide_ship_col = random_col(ship_board)
      hide_ship_direction = randint(0,1)
      if hide_ship_direction == 0: # horizontal
        ship_horizontal = 1
        ship_vertical = 0
      else: # vertical
        ship_horizontal = 0
        ship_vertical = 1
#      print hide_ship_direction
#      print ship_horizontal, ship_vertical
#      print hide_ship_row, hide_ship_col
      if ship_horizontal == 1:
        if ship_board[hide_ship_row][hide_ship_col] == "O" \
        and ((board_size - hide_ship_col - ship_size) * ship_horizontal) >= 0:
          empty = True
          for spot in range(hide_ship_col,hide_ship_col+ship_size):
            if ship_board[hide_ship_row][spot] <> "O":
              empty = False
      if ship_vertical == 1:
        if ship_board[hide_ship_row][hide_ship_col] == "O" \
        and ((board_size - hide_ship_row - ship_size) * ship_vertical) >= 0:
          empty = True
          for spot in range(hide_ship_row,hide_ship_row+ship_size):
            if ship_board[spot][hide_ship_col] <> "O":
              empty = False
    if ship_horizontal == 1:
        for loc in range(hide_ship_col,hide_ship_col+ship_size):
#          print loc
          ship_board[hide_ship_row][loc] = ship_initial
    if ship_vertical == 1:
        for loc in range(hide_ship_row,hide_ship_row+ship_size):
#          print loc
          ship_board[loc][hide_ship_col] = ship_initial

def hide_ships(fleet):
  for ship in fleet:
    hide_one_ship(ship)

def clear():
  print("\n" * 100)

# Variable initializations

ship_sizes = {"Aircraft Carrier" : 5, "Battleship" : 4, "Cruiser" : 3, \
"Submarine" : 3, "Destroyer" : 2}

ship_initials = {"Aircraft Carrier" : "A", "Battleship" : "B", "Cruiser" : "C", \
"Submarine" : "S", "Destroyer" : "D"}

ship_names = {"A" : "Aircraft Carrier", "B" : "Battleship", "C" : "Cruiser", \
"S" : "Submarine", "D" : "Destroyer"}

ship_hit_points = {"A" : 5, "B" : 4, "C" : 3, "S" : 3, "D" : 2}

turns = 0
board_size = 10
num_sunk = 0

num_ships = 0
for key in ship_sizes:
  num_ships = num_ships + 1
clear()

human_board = []
ship_board = []

for x in range(board_size):
  human_board.append(["O"] * board_size)
  ship_board.append(["O"] * board_size)

# Main routine

clear()
print "Welcome to Battleship!"
print
turns = int(raw_input("Number of turns allowed: "))
clear()

hide_ships(ship_sizes)
print_board(ship_board)

for turn in range(turns):
#  print_board(ship_board)
  print_board(human_board)
  print
  print "Turn", turn + 1, "of " + str(turns)
  guess_row = int(raw_input("Guess Row: "))-1
  guess_col = int(raw_input("Guess Col: "))-1
  clear()
  print
  if (guess_row < 0 or guess_row > board_size - 1) or \
  (guess_col < 0 or guess_col > board_size -1):
    print "Oops, that's not even in the ocean."
  elif (human_board[guess_row][guess_col] == "X" or \
  human_board[guess_row][guess_col] == "*"):
    print "You guessed that one already."
  elif ship_board[guess_row][guess_col] == "O":
    print "You missed my battleship!"
    human_board[guess_row][guess_col] = "X"
  else:
    ship_hit = ship_board[guess_row][guess_col]
    human_board[guess_row][guess_col] = "*"
    ship_name = ship_names[ship_board[guess_row][guess_col]]
    ship_hit_points[ship_board[guess_row][guess_col]] = \
    ship_hit_points[ship_board[guess_row][guess_col]] - 1
    print
    print "POW! That was a HIT!"
    print
    if ship_hit_points[ship_board[guess_row][guess_col]] == 0:
      num_sunk += 1
      print ship_name + " going down..."
      print
      print "You sank " + str(num_sunk) + \
      " of " + str(num_ships) + " ships!"
    if num_sunk == num_ships:
      print
      print_board(human_board)
      print
      print "Congratulations -- You Win!"
      print
      break
  if turn == turns-1:
    print
    print_board(human_board)
    print
    print "Game Over"
    print
    print "You sank " + str(num_sunk) + \
    " of " + str(num_ships) + " ships."
