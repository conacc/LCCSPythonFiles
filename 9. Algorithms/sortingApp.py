# sortingApp.py
# @coneill 09/09/2024

# Selection Sort Function
def selection(myList):
    for index in range(len(myList)-1): # loop runs 8 times(0->7)
        #print(myList)
        nextMinValue = min(myList[index+1:]) # find smallest value
        if nextMinValue < myList[index]: # If true, swap values
            nextMinIndex = myList.index(nextMinValue)
            myList[nextMinIndex] = myList[index]
            myList[index] = nextMinValue
    return myList
# Insertion Sort Function
def insertion(myList):
    for index in range(1, len(myList)):
        #print(myList)
        itemInsert = myList[index]
        position = index
        while position > 0 and myList[position-1] > itemInsert:
            myList[position] = myList[position-1]
            position -=1
        myList[position] = itemInsert
    return myList
# Bubble Sort Function
def bubble(myList):
    for outerIndex in range(len(myList) - 1):
        #print(myList)
        for index in range(len(myList) - 1):
            if myList[index] > myList[index+1]:
                tempValue = myList[index]
                myList[index] = myList[index+1]
                myList[index+1] = tempValue
    return myList
# Call the Functions
myList = [5,7,8,2,1,34,21,18,90,71] # initialise list
print("Original List:",myList)
print("Selection Sorted List:",selection(myList))
print("Insertion Sorted List:",insertion(myList))
print("Bubble Sorted List:",bubble(myList))
