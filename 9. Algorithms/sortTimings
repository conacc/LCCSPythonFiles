# sortTimings.py
# @coneill 11/09/2023
import time

# Create a function for each sorting type
def bubble(myList):
    for outerIndex in range(len(myList) - 1):
        print(myList)
        for index in range(len(myList) - 1):
            if myList[index] > myList[index+1]:
                tempValue = myList[index]
                myList[index] = myList[index+1]
                myList[index+1] = tempValue
    print(myList)
    
def insertion(myList):
    for index in range(1, len(myList)):
        print(myList)
        itemInsert = myList[index]
        position = index
        while position > 0 and myList[position-1] > itemInsert:
            myList[position] = myList[position-1]
            position -=1
        myList[position] = itemInsert
    print(myList)

def selection(myList):
    for index in range(len(myList)-1):
        print(myList)
        nextMinValue = min(myList[index+1:])
        if nextMinValue < myList[index]:
            nextMinIndex = myList.index(nextMinValue)
            myList[nextMinIndex] = myList[index]
            myList[index] = nextMinValue
    print(myList)

# Create a random list
import random
myList = []
for num in range(100):
    num1 = random.randint(1,100)
    myList.append(num1)
print(myList)
# Timed Bubble Sort
start = time.time()
bubble(myList)
end = time.time()
print("Bubble sort: ",end-start,"seconds")








