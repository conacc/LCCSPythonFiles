# rockPaperScissors.py
import random

lossCount = 0
winCount = 0

drawCount = 0



#starting screen for game
print("Hey! Welcome to my game,ROCK PAPER SCISSORS!")
#input that allows user to choose if they want to play
user_play_input = input('Would you like to play? (yes/no): ')

if user_play_input.lower() == 'no':
    print('Oh well,thats a shame...')
    quit()
    
     
elif user_play_input.lower() == 'yes':
   print("Well lets get it started then!")
#game mode selection
user_mode_input = input('What mode would you like to play? (singleplayer/multiplayer/sim): ')
user_mode_input = user_mode_input.lower()

#singleplayer mode
if user_mode_input == 'singleplayer':
    #input is given to pick between rock, paper pr scissors
    user_play_action = input("Pick between (rock, paper, scissors): ")
    possible_picks = ["rock", "paper", "scissors"]
    cpu_action = random.choice(possible_picks)
    print("Your opponent chose",cpu_action)
 
 
    if user_play_action == cpu_action:
            print("Both selected {user_play_action}. It's a tie!")
            drawCount += 1
    elif user_play_action == "rock":
            if cpu_action == "scissors":
                print("Rock smashes scissors! You win,Hooray!")
                winCount += 1
                
            else:
                print("Paper beats rock! You lose....Better luck next time!")
                lossCount += 1
               
    elif user_play_action == "paper":
            if cpu_action == "rock":
                print("Paper beats rock! You win,hooray!")
                winCount += 1
                
            else:
                print("Scissors beats paper! You lose....Better luck next time!")
                lossCount += 1
                
    elif user_play_action == "scissors":
            if cpu_action == "paper":
                print("Scissors beats paper! You win,hooray!")
                winCount += 1
               
            else:
                print("Rock beats scissors! You lose....Better luck next time!")
                lossCount += 1
     
#multiplayer game mode
elif user_mode_input == 'multiplayer':
    plyr1 = input("Enter a choice (rock, paper, scissors): ")
    plyr1 = plyr1.lower()

    print()

    plyr2 = input("Enter a choice (rock, paper, scissors): ")
    plyr2 = plyr2.lower()

    print()

    if (plyr1 == "rock"):
        if (plyr2 == "rock"):
            print("The game is a draw!")
            drawCount += 1
            
        elif (plyr2 == "paper"):
            print("Paper covers rock! Player 2 wins! ,Hooray!")
            winCount += 1
            
        elif (plyr2 == "scissors"):
            print("Rock smashes scissors! Player 1 wins!,Hooray!")
            winCount += 1
            
    elif (plyr1 == "paper"):
        if (plyr2 == "rock"):
            print("Paper covers rock! Player 1 wins!,Hooray!")
            winCount += 1
           
        elif (plyr2 == "paper"):
            print("The game is a draw!")
            drawCount += 1
           
        elif (plyr2 == "scissors"):
            print("Scissors cuts paper! Player 2 wins!,Hooray!")
    elif (plyr1 == "scissors"):
        if (plyr2 == "rock"):
            
            print("Rock smashes scissors! Player 2 wins!,Hooray!")
        elif (plyr2 == "paper"):
            print("Scissors cuts paper! Player 1 wins!,Hooray!")
        elif (plyr2 == "scissors"):
            print("The game is a draw")
            drawCount += 1
    
#simulation mode (cpu v cpu)
elif user_mode_input.lower() == 'sim':
   
    turns = 0
   
    while turns != 10:  
   
        possible_picks = ['rock','paper','scissors']
       
        computer_action = random.choice(possible_picks)
        print("computer 1 chose",computer_action)
       
        computer2_action = random.choice(possible_picks)
        print("computer 2 chose",computer2_action)
       
        if computer_action == computer2_action:
            print("Its a tie!")
            turns += 1
            break 
            
        if computer2_action== "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win,Hooray!")
                turns += 1
                break
                
            else:
                print("Paper covers rock! You lose....Better luck next time!")
                turns += 1
                break
                
        if computer2_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win,hooray!")
                turns += 1
                break
            
            else:
                print("Scissors cuts paper! You lose....Better luck next time!")
                turns += 1
                break
                
        if computer_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win,hooray!")
                turns += 1
                break
                
            else:
                print("Rock smashes scissors! You lose....Better luck next time!")
                turns += 1
                break

