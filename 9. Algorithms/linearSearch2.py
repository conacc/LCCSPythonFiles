# linearSearch2.py
# @coneill 06/10/2021
# Simple linear search (using for item in range)
myList = [1,3,7,2,9]
target = 2
for item in range(0,len(myList)):
    if myList[item] == target:
        location = item
print('Target found at index: ',location)  