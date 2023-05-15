# Poker.py

import csv


def storeResults(bet1, bet2, bet3, selectionTimebet1, selectionTimebet2,
                 selectionTimebet3, playerPoints, computerPoints):
  record = [
    bet1, bet2, bet3, selectionTimebet1, selectionTimebet2, selectionTimebet3,
    playerPoints, computerPoints
  ]
  file = open("results.csv", "a", newline="")
  r = csv.writer(file)
  r.writerow(record)
  file.close()
  print("New Record added to CSV")


# Greet player and tell them they are player 1
print('Welcome to Poker with Python')
print('You are Player 1')

# Ask what mode they want to play in

print('Choose your mode SINGLE/MULTIPLAYER/SIMULATION PLAY ')
gamemode = input('Enter mode: ')

gameMode = False

while gameMode == False:
  
  if gamemode.upper() == ('SINGLE'):
    
      gameMode = True
      
      # Generate points for both the computer and player
    
      playerPoints = int(100)
      computerPoints = int(100)
    
      while playerPoints < int(200) or computerPoints < int(200):
          
        input('\nPress the [enter key] to start the game')
    
        print('\n')
    
        import time
        import random
    
        print('You have', playerPoints, 'points')
        print('\n')
    
        card1 = random.randint(1, 12)
        card2 = random.randint(1, 12)
        card3 = random.randint(1, 12)
        playerCards = []
        playerCards.append(card1)
        playerCards.append(card2)
        playerCards.append(card3)
        print('Your cards are: ')
        print(playerCards)
    
        print('\n')
    
        # Create computers deck for singleplayer
        card4 = random.randint(1, 12)
        card5 = random.randint(1, 12)
        card6 = random.randint(1, 12)
        computerCards = []
        computerCards.append(card4)
        computerCards.append(card5)
        computerCards.append(card6)
    
        # Ask player to enter first bet(ante bet)
    
        print('How many points do you want to bet first?')
        print('Amounts are (10,5,1)')
        start1 = time.time()
        bet1 = int(input('Enter Amount here: '))
        bet20 = (0)
        while bet20 == 0:
          if bet1 == 10:
            bet20 = 0 + bet1
          elif bet1 == 5:
            bet20 = 0 + bet1
          elif bet1 == 1:
            bet20 = 0 + bet1
          else:
            bet1 = int(input('That is not a option try again: '))
        end1 = time.time()
        selectionTimebet1 = end1 - start1
        selectionTimebet1 = round(selectionTimebet1, 2)
    
        print('\n')
        # Create table deck of cards by dealer
    
        table1 = random.randint(1, 12)
        table2 = random.randint(1, 12)
        table3 = random.randint(1, 12)
        tableCards = []
        tableCards.append(table1)
        tableCards.append(table2)
        tableCards.append(table3)
        print('The table cards are: ')
        print(tableCards)
    
        print('\n')
    
        # Allow the player to bet again
    
        print('Now we will start the second round of betting')
        print('the Amounts are(5,10,15)')
        start2 = time.time()
        bet2 = int(input('Enter second bet here: '))
        bet21 = (0)
        while bet21 == 0:
          if bet2 == 5:
            bet21 = 0 + bet2
          elif bet2 == 10:
            bet21 = 0 + bet2
          elif bet2 == 15:
            bet21 = 0 + bet2
          else:
            bet2 = int(input('That is not a option try again: '))
        end2 = time.time()
        selectionTimebet2 = end2 - start2
        selectionTimebet2 = round(selectionTimebet2, 2)
    
        print('\n')
        # Tell player that one more card will be presented before final bet and let them continue
    
        print('The last table card will be presented now')
        input('\nPress the [enter key] to reveal final card')
    
        print('\n')
    
        # Create final table card to be presented to player
        table4 = random.randint(1, 12)
        tableCards.append(table4)
        print('The full table cards are: ')
        print(tableCards)
    
        print('\n')
    
        # Remind player of original deck before final bet
    
        print('Your full deck is now: ')
        print(playerCards, tableCards)
    
        print('\n')
    
        # Ask player for final bet
    
        print('The last round of betting will begin now')
        print('the Amounts are (10,15,20)')
        start3 = time.time()
        bet3 = int(input('Enter your final bet: '))
        bet22 = (0)
        while bet22 == 0:
          if bet3 == 10:
            bet22 = 0 + bet3
          elif bet3 == 15:
            bet22 = 0 + bet3
          elif bet3 == 20:
            bet22 = 0 + bet3
          else:
            bet3 = int(input('That is not a option try again: '))
        end3 = time.time()
        selectionTimebet3 = end3 - start3
        selectionTimebet3 = round(selectionTimebet3, 2)
    
        # Show the player their full bet amount and ask to see final result
    
        playerBet = int(bet1) + int(bet2) + int(bet3)
        computerBet = int(bet1) + int(bet2) + int(bet3)
        print('Your full bet amount is', playerBet)
        print('\n')
        print('We will now reveal both players cards')
        input('\nPress the [enter key] to reveal all cards')
    
        print('\n')
    
        # Reveal all decks
    
        print('Player 1 cards are', playerCards)
        print('The table cards are', tableCards)
        print('The computers cards are', computerCards)
    
        print('\n')
    
        finalplayerCards = playerCards + tableCards
        finalcomputerCards = computerCards + tableCards
    
        # Figure out score
        # importing
    
        from collections import Counter
    
        freq = Counter(finalplayerCards)
        n1 = 2
    
        playerPairs = 0
    
        if n1 in freq.values():
          for key, value in freq.items():
            if (value == n1):
              print("Player 1, {} is a pair ".format(key))
              playerPairs += 1
    
    # if no pairs are found
        else:
          print("Player 1 has no pairs")
    
        freq1 = Counter(finalcomputerCards)
        n2 = 2
    
        computerPairs = 0
    
        if n2 in freq1.values():
          for key, value in freq1.items():
            if (value == n2):
              print("Computer, {} is a pair ".format(key))
              computerPairs += 1
    
        else:
          print("Computer has no pairs")
    
        # Figure out who the winner is
    
        print('\n')
    
        if playerPairs > computerPairs:
          playerPoints += computerBet
          computerPoints -= playerBet
          print('Player 1 Wins the round')
          print('\n')
          print('Player 1 now has', playerPoints, 'points')
        elif playerPairs == computerPairs:
          print('Its a Draw')
        else:
          computerPoints += playerBet
          playerPoints -= computerBet
          print('Computer Wins the round')
          print('\n')
          print('Computer now has', computerPoints, 'points')
    
      #else:
        if playerPoints >= int(200):
          print('\n')
          print('PLayer 1 WINS THE GAME')
          storeResults(bet1, bet2, bet3, selectionTimebet1, selectionTimebet2,
                       selectionTimebet3, playerPoints, computerPoints)
        elif computerPoints >= int(200):
          print('\n')
          print('Computer WINS THE GAME')
          storeResults(bet1, bet2, bet3, selectionTimebet1, selectionTimebet2,
                       selectionTimebet3, playerPoints, computerPoints)
          break
        else:
          storeResults(bet1, bet2, bet3, selectionTimebet1, selectionTimebet2,
                       selectionTimebet3, playerPoints, computerPoints)
    
      # Generate points for both the computer and player
    
              
  elif gamemode.upper() == ('MULTIPLAYER'):
    
      gameMode = True
    
      player1Points = int(100)
      player2Points = int(100)
      while player1Points < int(200) or player2Points < int(200):
            
        print('\n')
      
        print('PLayer 1 cards will be revealed now player 2 look away')
      
        input('\nPress the [enter key] to start the game')
      
        print('\n')
      
        import random
      
        card1 = random.randint(1, 12)
        card2 = random.randint(1, 12)
        card3 = random.randint(1, 12)
        player1Cards = []
        player1Cards.append(card1)
        player1Cards.append(card2)
        player1Cards.append(card3)
        print('PLayer 1 cards are: ')
        print(player1Cards)
      
        print('\n')
        # Ask for Player 1 first bet
      
        print('How many points do you want to bet first?')
        print('Amounts are (10,5,1)')
        bet1 = int(input('Enter Amount here: '))
        bet23 = (0)
        while bet23 == 0:
          if bet1 == 10:
            bet23 = 0 + bet1
          elif bet1 == 5:
            bet23 = 0 + bet1
          elif bet1 == 1:
            bet23 = 0 + bet1
          else:
            bet1 = int(input('That is not a option try again: '))
      
      # Ask to reveal player 2 cards
      
        input('\nPress the [enter key] to reveal player 2 cards')
      
        # Create player 2 deck for multiplayer
        card4 = random.randint(1, 12)
        card5 = random.randint(1, 12)
        card6 = random.randint(1, 12)
        player2Cards = []
        player2Cards.append(card4)
        player2Cards.append(card5)
        player2Cards.append(card6)
      
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('PLayer 2 cards are: ')
        print(player2Cards)
      
        print('\n')
      
        # Ask player 2 to enter first bet
      
        print('How many points do you want to bet first?')
        print('Amounts are (10,5,1)')
        bet4 = int(input('Enter Amount here: '))
        bet24 = (0)
        while bet24 == 0:
          if bet4 == 10:
            bet24 = 0 + bet4
          elif bet4 == 5:
            bet24 = 0 + bet4
          elif bet4 == 1:
            bet24 = 0 + bet4
          else:
            bet4 = int(input('That is not a option try again: '))
      
      # Tell player 2 to reveal table cards for both players
      
        input('\nPress the [enter key] to reveal table cards for both players')
      
        # Hide player 2 cards
      
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
      
        # Create table deck of cards by dealer
      
        table1 = random.randint(1, 12)
        table2 = random.randint(1, 12)
        table3 = random.randint(1, 12)
        tableCards = []
        tableCards.append(table1)
        tableCards.append(table2)
        tableCards.append(table3)
        print('The table cards: ')
        print(tableCards)
      
        print('\n')
      
        # Allow player 1 to bet again
      
        print('Now we will start the seciond round of betting')
      
        print('\n')
      
        print('Player 1 will go first')
        print('the Amounts are(5,10,15)')
        bet2 = int(input('Enter second bet here: '))
        bet25 = (0)
        while bet25 == 0:
          if bet2 == 5:
            bet25 = 0 + bet2
          elif bet2 == 10:
            bet25 = 0 + bet2
          elif bet2 == 15:
            bet25 = 0 + bet2
          else:
            bet2 = int(input('That is not a option try again: '))
      
        print('\n')
      
        # Ask player 2 for their second bet
      
        print('Player 2 will now enter their second bet')
        print('the Amounts are(5,10,15)')
        bet5 = int(input('Enter second bet here: '))
        bet26 = (0)
        while bet26 == 0:
          if bet5 == 5:
            bet26 = 0 + bet5
          elif bet5 == 10:
            bet26 = 0 + bet5
          elif bet5 == 15:
            bet26 = 0 + bet5
          else:
            bet5 = int(input('That is not a option try again: '))
      
        print('\n')
        # Tell player that one more card will be presented before final bet and let them continue
      
        print('The last table card will be presented now')
        input('\nPress the [enter key] to reveal final card')
      
        # Create final table card to be presented to player
        table4 = random.randint(1, 12)
        tableCards.append(table4)
        print('The full table cards are: ')
        print(tableCards)
        print('\n')
      
        # Reveal Player 1 full deck and ask for final bet
        print('Player 2 look away while Player 1 enters their final bet')
        input('\nPress the [enter key] reveal Player 1 deck and bet')
      
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
      
        print('Player 1 full deck is now: ')
        print(player1Cards, tableCards)
      
        # Ask player for final bet
      
        print('The last round of betting will begin now')
        print('the Amounts are (10,15,20)')
        bet3 = int(input('Enter your final bet: '))
        bet27 = (0)
        while bet27 == 0:
          if bet3 == 10:
            bet27 = 0 + bet3
          elif bet3 == 15:
            bet27 = 0 + bet3
          elif bet3 == 20:
            bet27 = 0 + bet3
          else:
            bet3 = int(input('That is not a option try again: '))
      
        input('\nPress the [enter key] to hid your deck and bet')
      
        # Hide player 1 cards
      
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
      
        #Ask Player 2 for final bet and reveal their deck
      
        print('Now Player 1 will look away while Player 2 enters final bet')
      
        input('\nPress the [enter key] to Reveal Player 2 deck and bet')
      
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
      
        print('Player 2 full deck is now: ')
        print(player2Cards, tableCards)
      
        # Ask player for final bet
      
        print('The last round of betting will begin now')
        print('the Amounts are (10,15,20)')
        bet6 = int(input('Enter your final bet: '))
        bet28 = (0)
        while bet28 == 0:
          if bet6 == 10:
            bet28 = 0 + bet6
          elif bet6 == 15:
            bet28 = 0 + bet6
          elif bet6 == 20:
            bet28 = 0 + bet6
          else:
            bet6 = int(input('That is not a option try again: '))
      
        input('\nPress the [enter key] to hid your deck and bet')
      
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
      
        # Show the player their full bet amount and ask to see final result
      
        player1Bet = int(bet1) + int(bet2) + int(bet3)
        player2Bet = int(bet4) + int(bet5) + int(bet6)
        print('Player 1 full bet amount is', player1Bet)
      
        print('\n')
      
        print('Player 2 full bet amount is', player2Bet)
      
        print('\n')
      
        print('We will now reveal both players cards')
        input('\nPress the [enter key] to reveal all cards')
      
        print('\n')
      
        # Reveal all decks
      
        print('Player 1 cards are', player1Cards)
        print('The table cards are', tableCards)
        print('Player 2 cards are', player2Cards)
    
        print('\n')
    
        finalplayer1Cards = player1Cards + tableCards
        finalplayer2Cards = player2Cards + tableCards
    
        from collections import Counter
    
        freq = Counter(finalplayer1Cards)
        n1 = 2
    
        player1Pairs = 0
    
        if n1 in freq.values():
          for key, value in freq.items():
            if (value == n1):
              print("Player 1, {} is a pair ".format(key))
              player1Pairs += 1
    
    # if no pairs are found
        else:
          print("Player 1 has no pairs")
    
        freq1 = Counter(finalplayer2Cards)
        n2 = 2
    
        player2Pairs = 0
    
        if n2 in freq1.values():
          for key, value in freq1.items():
            if (value == n2):
              print("Player 2, {} is a pair ".format(key))
              player2Pairs += 1
    
    # if no pairs are found
        else:
          print("Player 2 has no pairs")
    
        print('\n')
    
        if player1Pairs > player2Pairs:
          player1Points += player2Bet
          player2Points -= player1Bet
          print('Player 1 Wins the round')
          print('\n')
          print('Player 1 now has', player1Points, 'points')
        elif player1Pairs == player2Pairs:
          print('Its a Draw')
        else:
          player2Points += player1Bet
          player1Points -= player2Bet
          print('Player 2 Wins the round')
          print('\n')
          print('Player 2 now has', player2Points, 'points')
    
      #else:
        if player1Points >= int(200):
          print('\n')
          print('PLayer 1 WINS THE GAME')
          
        elif player2Points >= int(200):
          print('\n')
          print('Player 2 WINS THE GAME')
          break
          
  elif gamemode.upper() == ('SIMULATION PLAY'):
    
      gameMode = True
    
      playerPoints = int(100)
      computerPoints = int(100)
    
      while playerPoints < int(200) or computerPoints < int(200):
    
        input('\nPress the [enter key] to start the game')
      
        import random
      
        card1 = random.randint(1, 12)
        card2 = random.randint(1, 12)
        card3 = random.randint(1, 12)
        playerCards = []
        playerCards.append(card1)
        playerCards.append(card2)
        playerCards.append(card3)
        print('\n')
        print('Your cards are: ')
        print(playerCards)
      
        # Create random deck for simulation play
      
        card4 = random.randint(1, 12)
        card5 = random.randint(1, 12)
        card6 = random.randint(1, 12)
        computerCards = []
        computerCards.append(card4)
        computerCards.append(card5)
        computerCards.append(card6)
      
        # Computer generates first bet(ante bet) for player
      
        print('How many points do you want to bet first?')
        print('Amounts are (10,5,1)')
        bet1options = ['10', '5', '1']
        bet1 = random.choice(bet1options)
      
        print('\n')
      
        print('Your first bet is:', bet1)
      
        print('\n')
      
        # Computer generates computer bet
      
        print('How many points do you want to bet first?')
        print('Amounts are (10,5,1)')
        bet4options = ['10', '5', '1']
        bet4 = random.choice(bet4options)
      
        # Create table deck of cards by dealer
      
        table1 = random.randint(1, 12)
        table2 = random.randint(1, 12)
        table3 = random.randint(1, 12)
        tableCards = []
        tableCards.append(table1)
        tableCards.append(table2)
        tableCards.append(table3)
        print('The table cards: ')
        print(tableCards)
      
        # Computer generates second bet for player
      
        print('Now we will start the seciond round of betting')
        print('the Amounts are(5,10,15)')
        bet2options = ['5', '10', '15']
        bet2 = random.choice(bet2options)
      
        print('\n')
      
        print('Your second bet is:', bet2)
      
        print('\n')
      
        # Computer generates second bet
      
        print('How many points do you want to bet first?')
        print('Amounts are (10,5,1)')
        bet5options = ['5', '10', '15']
        bet5 = random.choice(bet5options)
      
        # Tell player that one more card will be presented before final bet and let them continue
      
        print('The last table card will be presented now')
        input('\nPress the [enter key] to reveal final card')
      
        # Create final table card
        table4 = random.randint(1, 12)
        tableCards.append(table4)
        print('The full table cards are: ')
        print(tableCards)
      
        # Display full deck beside table cards
      
        print('Your full deck is now: ')
        print(playerCards, tableCards)
      
        # Computer generates final bet for player
      
        print('The last round of betting will begin now')
        print('the Amounts are (10,15,20)')
        bet3options = ['10', '15', '20']
        bet3 = random.choice(bet3options)
      
        print('\n')
      
        print('Your last bet is:', bet3)
      
        print('\n')
      
        # Computer generates final bet
      
        print('The last round of betting will begin now')
        print('the Amounts are (10,15,20)')
        bet6options = ['10', '15', '20']
        bet6 = random.choice(bet6options)
      
        # Show the player their full bet amount and ask to see final result
      
        playerBet = int(bet1) + int(bet2) + int(bet3)
        computerBet = int(bet4) + int(bet5) + int(bet6)
        print('\n')
        print('Your full bet amount is', playerBet)
      
        print('\n')
      
        print('We will now reveal both players cards')
        input('\nPress the [enter key] to reveal all cards')
      
        # Reveal all decks
      
        print('Player 1 cards are', playerCards)
        print('The table cards are', tableCards)
        print('The computers cards are', computerCards)
      
        print('\n')
      
        finalplayerCards = playerCards + tableCards
        finalcomputerCards = computerCards + tableCards
    
        # Figure out score
        # importing
    
        from collections import Counter
    
        freq = Counter(finalplayerCards)
        n1 = 2
    
        playerPairs = 0
    
        if n1 in freq.values():
          for key, value in freq.items():
            if (value == n1):
              print("Player 1, {} is a pair ".format(key))
              playerPairs += 1
    
    # if no pairs are found
        else:
          print("Player 1 has no pairs")
    
        freq1 = Counter(finalcomputerCards)
        n2 = 2
    
        computerPairs = 0
    
        if n2 in freq1.values():
          for key, value in freq1.items():
            if (value == n2):
              print("Computer, {} is a pair ".format(key))
              computerPairs += 1
    
    # If no pairs are found
        else:
          print("Computer has no pairs")
    
        # Figure out who the winner is
    
        print('\n')
    
        if playerPairs > computerPairs:
          playerPoints += computerBet
          computerPoints -= playerBet
          print('Player 1 Wins the round')
          print('\n')
          print('Player 1 now has', playerPoints, 'points')
        elif playerPairs == computerPairs:
          print('Its a Draw')
        else:
          computerPoints += playerBet
          playerPoints -= computerBet
          print('Computer Wins the round')
          print('\n')
          print('Computer now has', computerPoints, 'points')
    
      #else:
        if playerPoints >= int(200):
          print('\n')
          print('PLayer 1 WINS THE GAME')
          
        elif computerPoints >= int(200):
          print('\n')
          print('Computer WINS THE GAME')
          
          break
          
  else:
      input('That is not a gamemode try again: ')