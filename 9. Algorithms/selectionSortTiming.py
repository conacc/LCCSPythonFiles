# selectionSort.py
# @coneill 12/10/2021
# Sort a list using Selection Sort

#myList = [85,24,63,45,17,31,96,50]

# Create a random list
import random
myList = []
for i in range(1000):
    num = random.randint(1,10000)    
    if num not in myList:
        myList.append(num)
    
print(myList)

# Initialise two counter variables to zero
numRuns = 0
numSwaps = 0

# Measure start time
import time
startTime = time.time()

for index in range(len(myList)-1):
    # Increment run counter by 1
    numRuns = numRuns + 1
    print(myList)
    nextMinValue = min(myList[index+1:])
    if nextMinValue < myList[index]:
        # Increment swap counter by 1
        numSwaps += 1
        nextMinIndex = myList.index(nextMinValue)
        myList[nextMinIndex] = myList[index]
        myList[index] = nextMinValue
print(myList)
print("Number of runs:",numRuns)
print("Number of swaps:",numSwaps)
# Timing
print("Start Time:",startTime)
endTime = time.time()
print("End Time:",endTime)
print("Selection Sorting Time:",endTime - startTime,"seconds")