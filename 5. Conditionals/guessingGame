# guessingGame.py
# @coneill 16/12/2024
import random # library to generate random nums
userNum = input("Please enter number (1->10):")
if userNum.isdigit() == True:
    userNum = int(userNum)
    computerNum = random.randint(1,10)
    # print(userNum)
    # print(computerNum)
    if userNum > 10 or userNum < 0:
        print("INVALID ENTRY")
    elif userNum == computerNum:
        print("The computer chose",computerNum)
        print("WIN")
    elif userNum != computerNum: # != not equal to
        print("The computer chose",computerNum)
        print("LOSE")
else:
    print("Invalid entry")
