# timingSort.py
# @coneill 14/10/2021
# Timing of different sorting algorithms

# Create random list
import random 
randomList = [] 
x = 1000 # number of random numbers
y = 100 # maximum size of each number
for i in range(x): 
    r = random.randint(1,y) 
    randomList.append(r) 
print('Random List: ',randomList)

# Timing of Selection Sort
import time
start = time.time()
myList = randomList
for index in range(len(myList)-1):
    nextMinValue = min(myList[index+1:])
    if nextMinValue < myList[index]:
        nextMinIndex = myList.index(nextMinValue)
        myList[nextMinIndex] = myList[index]
        myList[index] = nextMinValue
end = time.time()
selectionTime = end-start

# Timing of Insertion Sort
start = time.time()
myList = randomList
for index in range(1, len(myList)):
    itemInsert = myList[index]
    position = index
    while position > 0 and myList[position-1] > itemInsert:
        myList[position] = myList[position-1]
        position -=1
    myList[position] = itemInsert
end = time.time()
insertionTime = end-start

# Timing of Bubble Sort
start = time.time()
myList = randomList
for outerIndex in range(len(myList) - 1):
    for index in range(len(myList) - 1):
        if myList[index] > myList[index+1]:
            tempValue = myList[index]
            myList[index] = myList[index+1]
            myList[index+1] = tempValue
end = time.time()
bubbleTime = end-start

# Timing of Quick Sort
start = time.time()
myList = randomList

def quickSort(listIn):
    if len(listIn) > 1:
        pivot = listIn[len(listIn)-1]
        belowPiv = []
        for item in listIn[:len(listIn) - 1]:
            if item < pivot:
                belowPiv.append(item)
        abovePiv = []
        for item in listIn[:len(listIn) - 1]:
            if item >= pivot:
                abovePiv.append(item)
        return quickSort(belowPiv) + [pivot] + quickSort(abovePiv)
    else:
        return listIn
quickSort(randomList)
end = time.time()
quickTime = end-start
print('Quicksort time: ',quickTime,'seconds')
print('Selection sort time: ',selectionTime,'seconds')
print('Insertion sort time: ',insertionTime,'seconds')
print('Bubble sort time: ',bubbleTime,'seconds')
