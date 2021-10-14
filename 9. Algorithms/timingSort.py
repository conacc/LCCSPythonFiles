# timingSort.py
# @coneill 14/10/2021
# Timing of different sorting algorithms

# Create random list
import random 
randomList = [] 
for i in range (100): 
    r = random.randint(1,100) 
    randomList.append(r) 
print(randomList)

# Timing of Selection Sort
import time
start = time.time()
myList = randomList
for index in range(len(myList)-1):
    print(myList)
    nextMinValue = min(myList[index+1:])
    if nextMinValue < myList[index]:
        nextMinIndex = myList.index(nextMinValue)
        myList[nextMinIndex] = myList[index]
        myList[index] = nextMinValue
print(myList)
end = time.time()
print('Selection sort time: ',end-start,'seconds')



