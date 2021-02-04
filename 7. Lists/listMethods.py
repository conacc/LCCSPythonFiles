# listMethods.py
# @coneill 03/02/2021
# Basic list methods
list.
# define a new list
myList = [87, 52, 7, 14]

# slicing
print(myList)
print(myList[2])
print(myList[1:])

# Appending and inserting

print(myList)
myList.append(75) # add to the end
print(myList)
myList.insert(2,88) # insert in an index position
myList.insert(5,88)
print(myList)
myList.remove(88)
print(myList)

# Index and count
myList.insert(2,88)
myList.insert(5,88)
print(myList)
counter = myList.count(88) # number of occurrances
print(counter)
myList.remove(88) # removes first 88
print(myList)
location = myList.index(88) # loc of first occurrance
print(location)


