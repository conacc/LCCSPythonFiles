from random import randint
import random
#original 2dimensional array to indentify the position on the board
B = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]
#change the column letter to the corresponding number
let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5}
num_to_let={0:'A',1:'B', 2:'C',3:'D', 4:'E',5:'F'}
#empty 2d array
Guess_Pattern=[[' ']*6 for x in range(6)]
#hidden 2d array containing the position of the ship
Real_Pattern=[[' ']*6 for x in range(6)]
       

print('WELCOME TO BATTLESHIPS')
row = randint(0,5)
column = randint(0,5)
#print('row',row)
#print('column',column)
#AIship = B[row][column]
#print('ship',AIship)


   
#extgen ==0 then extend the row
#extgen == 1 extend the column
#extgen ==0 then extend the row
#extgen == 1 extend the column
def ship_ext():
    extgen = randint(0,1)
    #print('extgen',extgen)
    ranNum3 = randint(0,1)
    #print('ranNum3',ranNum3)
   
   
   
    ranNum7 = randint(1,2)
    ranNum8 = randint(1,2)
    #to make the ship stay on the grid if it is near the edge
    if row == 0:
        if column==0:
            ranNum4=randint(0,1)
            if ranNum4 == 0:
                rowex1 = row+1
                colex1 = column
            elif ranNum4 == 1:
                colex1 = column+1
                rowex1 = row
        elif column==5:
            ranNum5=randint(0,1)
            if ranNum5 ==0:
                rowex1 = row+1
                colex1 = column
            elif ranNum5 == 1:
                colex1 = column-1
                rowex1=row
        elif column== 1 or 2 or 3 or 4:
            ranNum6 = randint(1,3)
            if ranNum6 == 1:
                colex1 = column-1
                rowex1 = row
            elif ranNum6 ==2:
                colex1 = column+1
                rowex1 = row
            elif ranNum6 == 3:
                rowex1 = row+1
                colex1 = column
#when the ship is on row 5 make it stay on the board
    if row == 5:
        if column == 0:
            if ranNum7 == 1:
                rowex1 = row-1
                colex1 = column
            elif ranNum7 == 2:
                colex1 = column +1
                rowex1 = row
        elif column == 5:
            if ranNum8 ==1:
                rowex1=row-1
                colex1=column
            elif ranNum8 ==2:
                colex1 = column-1
                rowex1=row
        elif column == 1 or 2 or 3 or 4:
            ranNum10 = randint(1,3)
            if ranNum10 == 1:
                colex1 = column
                rowex1 = row-1
            elif ranNum10 ==2:
                colex1 = column-1
                rowex1 = row
            elif ranNum10 == 3:
                rowex1 = row
                colex1 = column+1
           
#extending the ship while on column 0 to keep it on the board
    if column == 0:
        ranNum11 = randint(1,2)
        if row == 0:
            if ranNum11 == 1:
                colex1 = column+1
                rowex1 = row
            elif ranNum11 == 2:
                rowex1 = row+1
                colex1 = column
        elif row == 5:
            if ranNum11 == 1:
                colex1=column+1
                rowex1 = row
            elif ranNum11 == 2:
                rowex1 = row-1
                colex1=column
        elif row == 1 or 2 or 3 or 4:
            ranNum12 = randint(1,3)
            if ranNum12 == 1:
                colex1 = column
                rowex1 = row+1
            elif ranNum12 ==2:
                colex1 = column+1
                rowex1 = row
            elif ranNum12 == 3:
                rowex1 = row-1
                colex1 = column
# column 5 keep the ship on the board but still extending
    elif column ==5:
        ranNum13 = randint(1,2)
        if row == 0:
            if ranNum13 == 1:
                colex1 = column-1
                rowex1 = row
            elif ranNum13 == 2:
                rowex1 = row+1
                colex1 = column
        elif row == 5:
            if ranNum13 == 1:
                colex1=column-1
                rowex1 = row
            elif ranNum13 == 2:
                rowex1 = row-1
                colex1=column
        elif row == 1 or 2 or 3 or 4:
            ranNum14 = randint(1,3)
            if ranNum14 == 1:
                colex1 = column
                rowex1 = row+1
            elif ranNum14 ==2:
                colex1 = column-1
                rowex1 = row
            elif ranNum14 == 3:
                rowex1 = row-1
                colex1 = column
    else:
         if extgen == 0:
            #extending the row left or right.
            if ranNum3 == 1:
                rowex1=row+1
                colex1=column
            #elif ranNum3 == 0:
                #rowex1 = row
            elif ranNum3 == 0:
                rowex1 = row-1
                #print('rowext',rowex1)
                colex1=column
         #go up or down
         elif extgen == 1:
            if ranNum3 == 0:
                colex1 = column-1
                rowex1=row
           
            #elif ranNum3 == 0:
                #colex1 = column
            elif ranNum3 == 1:
                colex1 = column+1
            rowex1=row
    return int(rowex1),int(colex1)
rowex1,colex1 = ship_ext()
menu= int(input('Enter 1 if you choose to play, enter 0 if you choose to quit: '))
if menu ==0:
    print('You quit')
elif menu == 1:
    #play singleplayer, multiplayer or simulation
    gametype = int(input('Enter 1 for singleplayer, 2 for multiplayer or 3 for simulation: '))
    if gametype == 1:
        print('You chose single player')
        #userNum = input('chose a location to strike: ')
    elif gametype == 2:
        print('You chose multi-player')
        row = int(input('Enter a row from 1-6 :'))
        column = input('Enter a column from A-F: ').upper()
        column = let_to_num[column]
        row = row -1
        rowex1,colex1 = ship_ext()
        Real_Pattern[row][column] = 'X'
        Real_Pattern[rowex1][colex1] = 'X'
        def print_board(board):
            print('  A B C D E F')
            row_num=1
            for row in board:
                print('%d|%s|' % (row_num, '|'.join(row)))
                row_num +=1
    elif gametype == 3:
        print('You chose simulation play')
        #random row chosen
        row = randint(0,5)
        #random column chosen
        column = randint(0,5)
        #extension function
        rowex1,colex1 = ship_ext()
        #ship created
        Real_Pattern[row][column] = 'X'
        Real_Pattern[rowex1][colex1] = 'X'
        #board created
        def print_board(board):
            print('  A B C D E F')
            row_num=1
            for row in board:
                print('%d|%s|' % (row_num, '|'.join(row)))
                row_num +=1
        bot = 0
        def bot_guess():
            while bot == 0:
                row = randint(0,5)
                column = randint(0,5)
                return row,column
             #to keep the while loop going
        keepwhilegoing = 3
        # to count the amount of guesses
        guesscount = -1
        #to count the amount of ships hit
        guesscorrectcount = 0
        
        firstguesslist = []
        while keepwhilegoing == 3:
            print(print_board(Guess_Pattern))
            
            #get the row and column
            row,column = bot_guess()
            
            firstguesslist.append(row)
            firstguesslist.append(column)
            
            #print(firstguesslist)
            
            
            #firstguesscolumn =let_to_num[column]
            
            
            #increase the amount of guesses by 1
            guesscount = guesscount + 1
            #if the row and column chosen is the correct one in the real_pattern 2d array
            if Real_Pattern[row][column] == 'X':
                Real_Pattern[row][column] = 'P'
                Guess_Pattern[row][column] = 'X'
                print('HIT')
                guesscorrectcount = guesscorrectcount +1
            elif Guess_Pattern[row][column] == '-':
                print('You have already guessed this')
                guesscount = guesscount-1
            elif Real_Pattern[row][column] == 'P':
                print('You have already hit this ship.')
                guesscount = guesscount-1
            else:
                Guess_Pattern[row][column] = '-'
            if guesscorrectcount == 2:
                print(print_board(Guess_Pattern))
                print('Congratulations!')
                print('you have HIT both of the ships')
                print('it took you',guesscount,'attempts')
                guessrow = firstguesslist[0]
                firstguesscolumn = num_to_let[firstguesslist[1]]
                print('Your first row was',guessrow+1,'and your first column was',firstguesscolumn)
                import csv
                record = [guesscount,guessrow+1,firstguesscolumn]
                file = open("111354Database.csv","a",newline="")
                r = csv.writer(file)
                r.writerow(record)
                file.close()
                print("New Record added to CSV")
                quit()
           
       
        
       
   
    Real_Pattern[row][column] = 'X'
    Real_Pattern[rowex1][colex1] = 'X'
    def print_board(board):
        print('  A B C D E F')
        row_num=1
        for row in board:
            print('%d|%s|' % (row_num, '|'.join(row)))
            row_num +=1          
   

    def ship_loc():
        #Enter the row number between 1 to 8
        row =input('Please enter a ship row 1-6: ').upper()
        while row not in '123456':
            print('Please enter a valid row ')
            row=input('Please enter a ship row 1-6: ')
        #Enter the Ship column from A TO H
        column=input('Please enter a ship column A-F: ').upper()
        while column not in 'ABCDEF':
            print('Please enter a valid column ')
            column=input('Please enter a ship column A-F: ').upper()
        return int(row)-1,let_to_num[column]
    #to keep the while loop going
    keepwhilegoing = 3
    # to count the amount of guesses
    guesscount = 0
    #to count the amount of ships hit
    guesscorrectcount = 0
    #first guess
    firstguessvar = 1
    while keepwhilegoing == 3:
        while firstguessvar == 1:
            guessrow = int(input('Enter a row from 1 -6:'))
            guessrow = guessrow -1 
            guesscolumn = input('Enter a column from A-F:').upper()
            
            firstguesscolumn = guesscolumn
            guesscolumn = let_to_num[guesscolumn]
            
            
            if Real_Pattern[guessrow][guesscolumn] == 'X':
                Guess_Pattern[guessrow][guesscolumn] = 'X'
                print('well done you guessed it')
                guesscorrectcount = guesscorrectcount + 1
                guesscount = guesscount +1
                firstguessvar = firstguessvar - 1
            else:
                Guess_Pattern[guessrow][guesscolumn] = '-'
                guesscount = guesscount + 1
                firstguessvar = firstguessvar - 1
                print('Incorrect')
            print(print_board(Guess_Pattern))
        print(print_board(Guess_Pattern))
        #get the row and column
        row,column = ship_loc()
        #increase the amount of guesses by 1
        guesscount = guesscount + 1
        #if the row and column chosen is the correct one in the real_pattern 2d array
        if Real_Pattern[row][column] == 'X':
            Real_Pattern[row][column] = 'P'
            Guess_Pattern[row][column] = 'X'
            print('HIT')
            guesscorrectcount = guesscorrectcount +1
        elif Guess_Pattern[row][column] == '-':
            print('You have already guessed this')
        elif Real_Pattern[row][column] == 'P':
            print('You have already hit this ship')
        else:
            Guess_Pattern[row][column] = '-'
        if guesscorrectcount == 2:
            print(print_board(Guess_Pattern))
            print('Congratulations!')
            print('you have HIT both of the ships')
            print('it took you',guesscount,'attempts')
            print('first row',guessrow+1,'first column',firstguesscolumn)
            break
else:
    print('ERROR, enter a valid answer')
