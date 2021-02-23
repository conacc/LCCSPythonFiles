# fruitMachineActivitySolution.py
# @coneill 23/02/2021
# Program to simulate a fruit machine - Solution

import random

# initialise the list of fruits - 5 elements
fruits = ['Strawberry', 'Lemon', 'Orange', 'Raspberry', 'Cherry']

# generate three random numbers between 0 and 4 incl.
selection1 = random.randint(0, 4)
selection2 = random.randint(0, 4)
selection3 = random.randint(0, 4)

# show the results - display the fruits
print(fruits[selection1])
print(fruits[selection2])
print(fruits[selection3])

# Activity 1 - change the original code to ask a user to add a fruit
# name to the list, and then make the selections. Keep asking
# the user to add fruit until they type 'exit'
stop = ' '
while(stop != 'exit'):
    newFruit = input('Please enter a fruit to add to the list: ')
    fruits.append(newFruit)
    
    selection1 = random.randint(0, len(fruits))
    selection2 = random.randint(0, len(fruits))
    selection3 = random.randint(0, len(fruits))

    print(fruits[selection1])
    print(fruits[selection2])
    print(fruits[selection3])

    stop = input('Type exit to finish: ')

# Activity 2 - change the original code to tell the user that they
# win the €100 jackpot if all three selections are the same
# fruit, and that they win €10 if they match two

# generate three random numbers between 0 and the length of the list.
selection1 = random.randint(0, len(fruits))
selection2 = random.randint(0, len(fruits))
selection3 = random.randint(0, len(fruits))

# show the results - display the fruits
print(fruits[selection1])
print(fruits[selection2])
print(fruits[selection3])

if(selection1 == selection2 == selection3):
    print('You matched all three - you win €100')
elif(selection1 == selection2) or (selection1 == selection3) or (selection2 == selection3):
    print('You matched two - you win  €10')
else:
    print('You did not win')