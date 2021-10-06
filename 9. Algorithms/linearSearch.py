# linearSearch.py
# @coneill 06/10/2021
# Simple linear search (using for <variable> in <list>
myList = [1,3,7,2,9]
target = 2
count = 0
for value in myList:
    if value == target:
        location = count
    count+=1
print('Target found at index: ',location)