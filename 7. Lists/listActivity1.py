# listActivity1.py
# @coneill 02/02/2021
# Exercise on different options for adding to a list

# Insert a comment above each line explaining what it does

myList = [1, 2, 3, 4]

print(myList)

num = input('Enter a number to add to the list: ')
num = int(num)

myList.append(num)

# Insert a line so the user sees the list again


# Extension tasks: Insert the user's number at the start of the list,
# ask the user where in the list they would like the number to be inserted,
# check if the number is in the list already, and only add if it isn't,
# use a loop to keep asking the user for a number until they type 'exit'.