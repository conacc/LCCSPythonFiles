# randomNameGeneratorActivity.py
# @coneill 10/02/2021
# Generate random names (fill in the blanks)

# import the random library
import random

# create a list called firstNameList with two names in it
firstNameList = ['Alice', 'Bob']
print(firstNameList)

# create a list called secondNameList with two names in it


# Ask the user to add a name to the firstNameList
newName = input('Enter a first name to add to the list: ')
firstNameList.append(newName)
print(firstNameList)

# Ask the user to add a name to the secondNameList


# Generate two random numbers, and choose a name from each list
random1 = random.randint(0,len(firstNameList)-1)
randomFirst = firstNameList[random1]

#random2 = 
#randomSecond = 

#print('The random name generated is: ',randomFirst, randomSecond)

