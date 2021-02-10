# fruitMachineActivity.py
# @coneill 10/02/2021
# Program to simulate a fruit machine!

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


# Activity 2 - change the original code to tell the user that they
# win the €100 jackpot if all three selections are the same
# fruit, and that they win €10 if they match two
