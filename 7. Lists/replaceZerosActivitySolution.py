# replaceZerosActivitySolution.py
# @coneill 23/02/2021
# Replace zeros in a list
# Solution to activity

# Create a list with ten numbers, at least three zeros
myList = [2, 6, 7, 56, 0, 3, 68, 99, 0, 0]

# Print the list to the screen
print('Here is the list:\n', myList)

# Use a for loop to go through the list and replace any
# zeros with the number 100
for i in range(len(myList)):
    if myList[i] == 0:
        myList[i] = 100

# Print the list to the screen again to show it works
print('Here is the list with zeros replaced by 100s:\n', myList)