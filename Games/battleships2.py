import csv
import random
import time
import pandas as pd

file = open('results.csv','a',newline='')
file.close()
endG1 = True # Boolean, allows the game to be played over and over until it turns False
while endG1 == True:
    freeList = [] # positions for player 1
    freeList2 = [] # guesses
    freeList3 = [] # gamemodes
    freeList4 = [] # positions for player 2
    lts_to_nums = {'A': 0,'B': 1,'C': 2,'D': 3,'E': 4}
    listCPU = ['A','B','C','D','E']
    numCPU = [1,2,3,4,5]
    numList = ['A1','A2','A3','A4','A5','B1',]
    numList2 = numList
    times = 0 # How many guesses it takes
    times2 = 0 # How many guesses it takes
    guesses = 0 # counting how many ships have sunk
    guesses2 = 0 # counting how many ships have sunk
    num1 = 0 # counts how many ships have been placed on the board
    num2 = 0 # counts how many ships have been placed on the board
    count = 0
    count2 = 0
    # Boards for players to place their ships
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ]

    board2 = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ]
    # Boards for guessing the other players position
    guesses_board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ]
    guesses2_board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ]


    def player1_positions():#Function that creates ships for the user and for CPU/user to guess their ships
        if n1 == True:
            column = input("column (A to E):")
            column = column.upper()
            while column not in "ABCDE":
                print("There is no such column! It should be A, B, C, D or E")
                column = input("column (A to E):")
                column = column.upper()
            while column == '':
                print("There is no such column! It should be A, B, C, D or E")
                column = input("column (A to E):")
                column = column.upper()
            x2 = str(column)    
            row = input("row (1 to 5):")
            while row not in "12345":
                print("There is no such row! It should be 1, 2, 3, 4 or 5")
                row = input("row (1 to 5):")
            while row == '':
                print("There is no such row! It should be 1, 2, 3, 4 or 5")
                row = input("row (1 to 5):")  
            y = row
        elif n1 == False:
             column = random.choice(listCPU)
             while column not in "ABCDE":
                column = random.choice(listCPU)
             row = random.choice(numCPU)
             row = str(row)
             while row not in "12345":
                 row = random.choice(numCPU)
        if n1 == True:
            xy = x2+y
            freeList.append(xy)  
        return int(row) - 1, lts_to_nums[column]
    def player2_positions(): #Function that creates ships for player 2
        column2 = input("column (A to E):")
        column2 = column2.upper()
        while column2 not in "ABCDE":
            print("There is no such column! It should be A, B, C, D or E")
            column2 = input("column (A to E):")
            column2 = column2.upper()
        while column2 == '':
                print("There is no such column! It should be A, B, C, D or E")
                column2 = input("column (A to E):")
                column2 = column2.upper()
        x1 = column2
        row2 = input("row (1 to 5):")
        while row2 not in "12345":
            print("There is no such row! it should be 1, 2, 3, 4 or 5")
            row2 = input("row (1 to 5):")
        while row2 == '':
            print("There is no such row! it should be 1, 2, 3, 4 or 5")
            row2 = input("row (1 to 5):")
        y1 = row2
        xy2 = x1+y1
        freeList4.append(xy2)
        return int(row2) - 1, lts_to_nums[column2]
    def CPU2_positions():#Function that creates ships for the CPU
        column = random.choice(listCPU) # Allows randomness
        while column not in "ABCDE":
            column = random.choice(listCPU)
        x2 = column
        row = random.choice(numCPU)
        row = str(row)
        while row not in "12345":
            row2 = random.choice(numCPU)
        y = row
        xy = x2+y
        freeList.append(xy)
        return int(row) - 1, lts_to_nums[column]
    def CPU1_positions(): #Function that creates ships for the CPU
        if n == False:
            column2 = input("column (A to E):")
            column2 = column2.upper()
            while column2 not in "ABCDE":
                print("There is no such column! It should be A, B, C, D or E")
                column2 = input("column (A to E):")
                column2 = column2.upper()
            while column2 == '':
                print("There is no such column! It should be A, B, C, D or E")
                column2 = input("column (A to E):")
                column2 = column2.upper()
                
            row2 = input("row (1 to 5):")
            while row2 not in "12345":
                print("There is no such row! it should be 1, 2, 3, 4 or 5")
                row2 = input("row (1 to 5):")
            while row2 == '':
                print("There is no such row! it should be 1, 2, 3, 4 or 5")
                row2 = input("row (1 to 5):")
        elif n == True:
            column2 = random.choice(listCPU)
            while column2 not in "ABCDE":
                column2 = random.choice(listCPU)
            x1 = column2
            row2 = random.choice(numCPU)
            row2 = str(row2)
            while row2 not in "12345":
                row2 = random.choice(numCPU)
                row2 = str(row2)
                numList.remove(row2)
            y1 = row2
        if n == True:
            xy2 = x1+y1
            freeList4.append(xy2)
        return int(row2) - 1, lts_to_nums[column2]
    def continue1():
        enter = input('Press enter to continue')
        if enter == ' ':
            print(' ')
        
    def data_saving():
        file = open("results.csv","a",newline="")
        r = csv.writer(file)
        record = [freeList[0],freeList[1],freeList[2],freeList[3],freeList[4],guessNum,userC1]
        r.writerow(record)
        record1 = [freeList4[0],freeList4[1],freeList4[2],freeList4[3],freeList4[4],0,0]
        r.writerow(record1)
        file.close()
    def game_board(board):# function defined for the board to be made and printed for battleship
        print('Board no.1') # The board that places the first players ships and used to be guessed on by the second player
        print("  A B C D E ")
        print(" +-+-+-+-+-+")
        row_num = 1
        for row in board:
            print("%d|%s|" % (row_num, "|".join(row)))
            print(" +-+-+-+-+-+")
            row_num = row_num + 1

    def game_board2(board2):# function defined for the board to be made and printed for battleship
        print('Board no.2') # The board that places the second players ships and used to be guessed on by the first player player
        print("  A B C D E ")
        print(" +-+-+-+-+-+")
        row_num2 = 1
        for row2 in board2:
            print("%d|%s|" % (row_num2, "|".join(row2)))
            print(" +-+-+-+-+-+")
            row_num2 = row_num2 + 1
            
    

    print(' ')
    print('*************Welcome to Battleship*************')
    print(' ')


    print('Let us begin the battle! Choose your game mode') # user chooses which gamemode they wish to play

    print('1- Singleplayer') # user1 vs CPU1

    print('2- Multiplayer') # user1 vs user2

    print('3- How To Play') # CPU1 vs CPU2
    userC1 = input('Enter 1, 2 or 3: ')
    while userC1 not in "123":
        print('invalid option')
        userC1 = input('Enter 1, 2 or 3: ')
        
    userC1 = int(userC1)
    if userC1 == 1:
        print('Welcome to Singleplayer mode')
        userName1 = input('Player 1:')
        userName1 = userName1.lower()
        userName1 = userName1.capitalize()
        while num1 < 5:
            n1 = True
            print("Where do you want ship ", num1 + 1,userName1, "?")
            row_num, column_num = player1_positions()
            num1 = num1 + 1
           # Check that there are no repeats
            if board[row_num][column_num] == 'X':
                print("That spot already has a battleship in it!")
                num1 = num1-1
        
            board[row_num][column_num] = 'X'
            game_board(board)
        while num2 < 5:
            n = True
            row_num2, column_num2 = CPU1_positions()
            num2 = num2 + 1

           # Check that there are no repeats
            if board2[row_num2][column_num2] == 'X':
                num2 = num2-1
            board2[row_num2][column_num2] = 'X'
            game_board2(board2)
            turn = 'Player1'
            endF1 = True
        print("\n"*30)
        print('Board no.1: CPUs Guesses')
        print('Board no.2: Player1s Guesses')
        while endF1 == True:
            numCPU = [1,2,3,4,5]
            if turn == 'Player1':
                n = False
                game_board2(guesses_board)
                print("Guess a battleship location",userName1)
                row_num2, column_num2 = CPU1_positions()

                if guesses_board[row_num2][column_num2] != ' ':
                    print("You have already guessed that place!")
                    continue

                # Check that there are no repeats
                if board2[row_num2][column_num2] == 'X':
                    guesses_board[row_num2][column_num2] = 'X'
                    guesses = guesses + 1
                    times = times + 1
                    game_board2(guesses_board)
                    print("\n"*30)
                    print("HIT!")
                    
                    
                else:
                    guesses_board[row_num2][column_num2] = '.'
                    times = times + 1
                    turn = 'CPU1'
                    game_board2(guesses_board)
                    print("\n"*30)
                    print("MISS!")

            elif turn == 'CPU1': # CPU's turn
                n1 = False
                row_num, column_num = player1_positions()
                if guesses2_board[row_num][column_num] != ' ':
                    continue
                # Check that there are no repeats
                if board[row_num][column_num] == 'X':
                    print("HIT!")
                    guesses2_board[row_num][column_num] = 'X'
                    guesses2 = guesses2 + 1
                    times2 = times2 + 1
                    game_board(guesses2_board)
                    
                else:
                    guesses2_board[row_num][column_num] = '.'
                    print("MISS!")
                    times2 = times2 + 1
                    turn = 'Player1'
                    game_board(guesses2_board)
                    print("\n"*30)
            if guesses == 5:
                print(userName1,' wins!')
                guessNum = times
                break
                
            elif guesses2 == 5:
                print('CPU wins!')
                guessNum = times2
                break
        playAgain = input('Play again?(Yes or No?)')
        playAgain = playAgain.lower()
        i = True
        while i == True:
            if playAgain == 'yes':
                data_saving()
                i = False
                endG1 = True
            elif playAgain == 'no':
                data_saving()
                i = False
                endG1 = False
                print('Thank you for playing!')
            else:
                print('Invalid option')
                playAgain = input('Play again?(Yes or No?)')
                playAgain = playAgain.lower()

    elif userC1 == 2:
        print('Welcome to Multiplayer mode')
        freeList3.append(userC1)

        userName1 = input('Player 1:')
        userName1 = userName1.lower()
        userName1 = userName1.capitalize()
        userName2 = input('Player 2:')
        userName2 = userName2.lower()
        userName2 = userName2.capitalize()
        
        while num1 < 5:
            n1 = True
            print("Where do you want ship ", num1 + 1,userName1, "?") # player 2 looks away
            row_num, column_num = player1_positions()
            num1 = num1 + 1

           # Check that there are no repeats
            if board[row_num][column_num] == 'X':
                print("That spot already has a battleship in it!")
                num1 = num1-1
       
            board[row_num][column_num] = 'X'
            game_board(board)
        
        print("\n"*30)
        print("player 2's board") # Player 1 looks away
        
        while num2 < 5:
           print("Where do you want ship ", num2 + 1,userName2, "?")
           row_num2, column_num2 = player2_positions()
           num2 = num2 + 1

           # Check that there are no repeats
           if board2[row_num2][column_num2] == 'X':
                print("That spot already has a battleship in it!")
                num2 = num2-1
       
           board2[row_num2][column_num2] = 'X'
           game_board2(board2)   
        
        print("\n"*30)
        print('Board no.2:',userName1,'s guesses')
        print('Board no.1:',userName2,'s guesses')
        turn = 'player1'
        endF1 = True
        while endF1 == True:
           if turn == 'player1':
               game_board2(guesses_board)
               print("Guess a battleship location",userName1)
               row_num2, column_num2 = player2_positions()

               if guesses_board[row_num2][column_num2] != ' ':
                   print("You have already guessed that place!")
                   continue

                # Check that there are no repeats
               if board2[row_num2][column_num2] == 'X':
                   guesses_board[row_num2][column_num2] = 'X'
                   guesses = guesses + 1
                   times = times + 1
                   game_board2(guesses_board)
                   print("\n"*30)
                   print(userName1,"HIT!")
               else:
                   guesses_board[row_num2][column_num2] = '.'
                   times = times + 1
                   game_board2(guesses_board)
                   turn = 'player2'
                   print("\n"*30)
                   print(userName1,"MISS!")

           elif turn == 'player2':
               game_board(guesses2_board)
               print("Guess a battleship location",userName2)
               row_num, column_num = player1_positions()

               if guesses2_board[row_num][column_num] != ' ':
                   print("You have already guessed that place!")
                   continue

                # Check that there are no repeats
               if board[row_num][column_num] == 'X':
                   guesses2_board[row_num][column_num] = 'X'
                   guesses2 = guesses2 + 1
                   times2 = times2 + 1
                   game_board(guesses2_board)
                   print("\n"*30)
                   print(userName2,"HIT!")
               else:
                   guesses2_board[row_num][column_num] = '.'
                   times2 = times2 + 1
                   game_board(guesses2_board)
                   turn = 'player1'
                   print("\n"*30)
                   print(userName2,"MISS!")
               
           if guesses == 5:
               print(userName1,'wins!')
               guessNum = times
               endF1 = False
            
           elif guesses2 == 5:
               print(userName2,'wins!')
               guessNum = times2
               endF1 = False
        playAgain = input('Play again?(Yes or No?)')
        playAgain = playAgain.lower()
        i = True
        while i == True:
            if playAgain == 'yes':
                data_saving()
                i = False
                endG1 = True
            elif playAgain == 'no':
                data_saving()
                i = True
                endG1 = False
                print('Thank you for playing!')
                break
            else:
                print('Invalid option')
                playAgain = input('Play again?(Yes or No?)')
                playAgain = playAgain.lower()
    elif userC1 == 3:
        print('How to Play (Simulation)')
        freeList3.append(userC1)
        print('First place your five ships')
        continue1()
        print('CPU1 chooses')
        while num2 < 5:
            n = True
            row_num2, column_num2 = CPU1_positions()
            num2 = num2 + 1
    
           # Check that there are no repeats
            if board2[row_num2][column_num2] == 'X':
                num2 = num2-1
            board2[row_num2][column_num2] = 'X'
            game_board2(board2)
            continue1()
        
        print("\n"*8)
        print('CPU2 chooses')
        continue1()
        while num1 < 5:
            row_num, column_num = CPU2_positions()
            num1 = num1 + 1

           # Check that there are no repeats
            if board[row_num][column_num] == 'X':
                num1 = num1-1
            board[row_num][column_num] = 'X'
            game_board(board)
            continue1()
        turn = 'CPU1'
        endF1 = True
        print("\n"*30)
        print('Now they have to guess where the other players ships are')
        continue1()
        print('CPU1s turn')
        while endF1 == True:
            numCPU = [1,2,3,4,5]
            if turn == 'CPU1':
                row_num, column_num = CPU2_positions()

                if guesses2_board[row_num][column_num] != ' ':
                    continue

                # Check that there are no repeats
                if board[row_num][column_num] == 'X':
                    print("CPU1 HIT!")
                    guesses2_board[row_num][column_num] = 'X'
                    guesses2 = guesses2 + 1
                    times2 = times2 + 1
                    
                    
                else:
                    guesses2_board[row_num][column_num] = '.'
                    print("CPU1 MISS!")
                    print('CPU2s turn')
                    turn = 'CPU2'
                    times2 = times2 + 1
                game_board(guesses2_board)
            elif turn == 'CPU2':
                row_num2, column_num2 = CPU1_positions()
                
                if guesses_board[row_num2][column_num2] != ' ':
                    continue
                # Check that there are no repeats
                if board2[row_num2][column_num2] == 'X':
                    print("CPU2 HIT!")
                    guesses_board[row_num2][column_num2] = 'X'
                    guesses = guesses + 1
                    turn = 'CPU2'
                    times = times + 1
        
                        
                else:
                    guesses_board[row_num2][column_num2] = '.'
                    print("CPU2 MISS!")
                    print('CPU1s turn')
                    turn = 'CPU1'
                    times = times + 1
                game_board2(guesses_board)
            if guesses == 5:
                print('CPU 2 wins!')
                guessNum = times
                endF1 = False

                
            elif guesses2 == 5:
                print('CPU 1 wins!')
                guessNum = times2
                endF1 = False
        playAgain = input('Play again?(Yes or No?)')
        playAgain = playAgain.lower()
        i = True
        while i == True:
            if playAgain == 'yes':
                data_saving()
                i = False
                endG1 = True
            elif playAgain == 'no':
                data_saving()
                i = True
                endG1 = False
                print('Thank you for playing!')
                break
            else:
                print('Invalid option')
                playAgain = input('Play again?(Yes or No?)')
                playAgain = playAgain.lower()
