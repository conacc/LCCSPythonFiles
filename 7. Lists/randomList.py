# randomList.py
# @coneill 10/02/2021
# Use the random function to choose an element from a list

import random
myList = ['a', 'b', 'c']
myList.append('d')
print(myList)
choice = random.randint(0,len(myList)-1)
print(myList[choice])