from random import randint # Imports randint function
board = [] # Creates global board list
for x in range(5):
  board.append(["O"] * 5)
  # This function adds 5 "0"s per cycle, there are 5 cycles
row = randint(0,5)
column = randint(0,5)
score = 25

def print_board(board):
  for row in board:
    print( " ".join(row))
    # This function iterates through each "O" list and adds a space between
    # This iteration prints on a new line every time a new sub-list is found
def random_row(board):
    return randint(0, len(board) - 1)

    
  # This function selects a random list based on the number of sub-lists in the
  # Board list
def random_col(board):
  return randint(0, len(board[0]) - 1)
  # This function selects a random element in the first sub-list of the
  # Board list. This can be applied to every list, hence the column creation
ship_row = random_row(board) # Sets the row (x) position of the ship
ship_col = random_col(board) # Sets the column (y) position of the ship
def game():
    print_board(board) # Prints the board
    for turn in range(25): # Begins player V CPU cycle, does so 4 times
        guess_row = int(input("Guess Row: ")) # Prompts user for row (x) guess, then converts to int
        guess_col = int(input("Guess Col: ")) # Promps user for column (y) guess, then converts to int
        guess_row -= 1 # Brings guess down by one to account for CPU guess and board size
        guess_col -= 1 # "                                                              "
        if guess_row == ship_row and guess_col == ship_col: # Checks if player guess is same as randomly generated ship position
            print ("Congratulations! You sunk my battleship!") # Prints out win message
            break # Cuts if statement and ends game
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): # Checks if user guess is outside of board
                print ("Oops, that's not even in the ocean.") # Prints invalid pos message
            elif(board[guess_row][guess_col] == "X"): # Checks if user already guessed a position
                print ("You guessed that one already.") # Prints redundancy message
            else: # nested else statement covers if player missed the CPU ship
                print ("You missed my battleship!") # Prints miss message
                board[guess_row][guess_col] = "X" # Sets board according to (incorrect) player guess_row
                print("---Turn", turn + 1, "---") # Prints turn number
                if turn == 3: # Checks to see if turn number is 3, then ends the game
                    print ("Game Over")
            print_board(board) # Prints board if battleship is not sunk
def main():
    player = 0 # Sets player variable
    print ("Welcome to battleship!") # Prints welcome message
    player = int(input("Enter 1 for Single player or 2 for Multiplayer or 3 for Simulated play:")) # Takes input to decide number of players
#-----------------------------------------------------------------------------------------------------------------    
    if player == 1:
        game()
       
    # Starts single player game if only one player is selected

    elif player == 3:
        print('Welcome to simulated play')
        print_board(board)
        for turn in range(11): # Starts turn loop
            row= randint(0,4)
            column=randint(0,4)
            print( "---Turn", turn + 1, "---") # Prints turn every time
            if (row == ship_row) and (column == ship_col): # Checks to see if X coordinate guess and Y coordinate guess equals player one's selection
                board[row][column] = "X" # Sets an X at the point of selection
                print_board(board) # Prints the board
                print ("Congratulations! You sunk their battleship!")# Prints victory message
                print('You win')
                break # Exits if statement
            elif board[row][column] == "X": # Checks to see if the player guessed a spot already
                print ("You already guessed that!")# Prints appropriate message
            else:
                 print ("You missed their battleship!") # If else, prints message that the battleship was missed
                 board[row][column] = "X" # Sets guess X Y coord to an X
                 if turn == 10: # Checks to see if turn 3 has been reached
                     print ("Game Over") # Prints game over message
            print_board(board) # Prints board
            
        
    elif player == 2:
        print ("Welcome to the 2 player version of battleship, you will be facing head on with another human player!")
        print ("Get ready to pass the comp!")
        print_board(board)
        print(ship_row,",",ship_col)
        print ("Player one:")
        player_one_row_selection = int(input("Please select a row:")) - 1
        player_one_col_selection = int(input("Please select a column:")) - 1
        print ("Player two:")
        # Prints 2 player welcome message, prints the board, and then promps player one for the battleship position
        for turn in range(25): # Starts turn loop
            print( "---Turn", turn + 1, "---", score - 1) # Prints turn every time
            player_two_row_guess = int(input("Please select a row:")) - 1 # Takes input from player 2 for Turn n for row
            player_two_col_guess = int(input("Please select a column:")) - 1 # Takes input from player 2 for Turn n for column
            if (player_two_row_guess == player_one_row_selection) and (player_two_col_guess == player_one_col_selection): # Checks to see if X coordinate guess and Y coordinate guess equals player one's selection
                board[player_two_row_guess][player_two_col_guess] = "X" # Sets an X at the point of selection
                print_board(board) # Prints the board
                print ("Congratulations! You sunk their battleship!")# Prints victory message
                print('Player 1 Wins!')
                break # Exits if statement
            elif (player_two_row_guess < 0 or player_two_row_guess > 4) or (player_two_col_guess < 0 or player_two_col_guess > 4): # Checks to see if guess is out of bounds
                 print ("Thats out of bounds!") # Prints out of bounds message
            elif board[player_two_row_guess][player_two_col_guess] == "X": # Checks to see if the player guessed a spot already
                print ("You already guessed that!") # Prints appropriate message
            else:
                 print ("You missed their battleship!") # If else, prints message that the battleship was missed
                 board[player_two_row_guess][player_two_col_guess] = "X" # Sets guess X Y coord to an X
                 if turn == 10: # Checks to see if turn 3 has been reached
                     print ("Game Over") # Prints game over message
            print_board(board) # Prints board
    else: # If player enters something other than 1 or 2 it prints a message
        print ("Please come back and select a valid number!") # prints "number invalid" message
main() # Starts game



