# randomNumberGuesser.py
# @coneill 22/10/2025

# Random library
import random
# Ask for user name
name = input("Enter your name: ")
# Ask user to guess
userNum = input("Enter a guess between 1 and 10: ")
if userNum.isdigit() == True:
    userNum = int(userNum)
    if userNum > 0 and userNum < 11:  
        print("You chose the number",userNum)
        # Generate random number
        computerNum = random.randint(1,10)
        print("The computer chose",computerNum)
        # Check if user guess is correct
        if userNum == computerNum:
            winner = name
        elif userNum != computerNum:
            winner = "Computer"
        # Print final result
        print("The winner was: "+winner)
    else:
        print("Invalid number")
else:
    print("That is not a number")
