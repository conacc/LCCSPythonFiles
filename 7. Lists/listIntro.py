# listIntro.py
# @coneill 25/01/2022
# List types and methods
'''
# List of integers
myList = [3, 6, 45, -19]
print(myList) # print full list
# print(myList[0]) # print first value
# print(len(myList)) # length of list
myList.append(42) # add to end of list
print(myList)
myList.insert(2, -167)# add at a chosen place 
print(myList)
'''
# List of strings
myList = ['apple','orange','pear']
print(myList)
myList.append('banana')
print(myList)
import random
choice = random.randint(0,len(myList)-1)
print('The chosen fruit is:')
print(myList[choice])
    
    
    
    




