# listActivity1Solution.py
# @coneill 09/02/2021
# Solution to activity

# Insert a comment above each line explaining what it does

# Creates a list called myList
myList = [1, 2, 3, 4]

# Prints list to screen
print(myList)

# Asks user for a number, stores as variable
num = input('Enter a number to add to the list: ')
# Convert string to integer
num = int(num)

# Add num to end of list
myList.append(num)

# Insert a line so the user sees the list again
print(myList)

# Extension tasks:
#Insert the user's number at the start of the list
myList.insert(0,num)
print(myList)

# ask the user where in the list they would like the number to be inserted:
num = input('Enter a number to add to the list: ')
num = int(num)
pos = input('Enter position in list to insert number: ')
pos = int(pos)
myList.insert(pos,num)
print(myList)

# check if the number is in the list already, and only add if it isn't
num = input('Enter a number to add to the list: ')
num = int(num)
pos = input('Enter position in list to insert number: ')
pos = int(pos)
if myList.count(num) == 0:
    myList.insert(pos,num)
    print('Number inserted')
    print(myList)
else:
    print('Number is already in list, not inserted')
# use a loop to keep asking the user for a number until they type 'exit'.
repeat = ' '
while(repeat != 'exit'):
    num = input('Enter a number to add to the list: ')
    num = int(num)
    pos = input('Enter position in list to insert number: ')
    pos = int(pos)
    print(myList)
    repeat = input('Type exit if you do not want to continue: ')
