# randomNameGeneratorActivitySolution.py
# @coneill 23/02/2021
# Generate random names - Solution

# import the random library
import random

# create a list called firstNameList with two names in it
firstNameList = ['Alice', 'Bob']
print(firstNameList)

# create a list called secondNameList with two names in it
secondNameList = ['Murphy', 'Osaka']
print(secondNameList)

# Ask the user to add a name to the firstNameList
newName = input('Enter a first name to add to the list: ')
firstNameList.append(newName)
print(firstNameList)

# Ask the user to add a name to the secondNameList
newName = input('Enter a second name to add to the list: ')
secondNameList.append(newName)
print(secondNameList)

# Generate two random numbers, and choose a name from each list
random1 = random.randint(0,len(firstNameList)-1)
randomFirst = firstNameList[random1]

random2 = random.randint(0,len(secondNameList)-1)
randomSecond = secondNameList[random2]

print('The random name generated is: ',randomFirst, randomSecond)

