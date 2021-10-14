# insertionSort.py
# @coneill 12/10/2021
# Sort a list using Insertion Sort
myList = [85,24,63,45,17,31,96,50]
for index in range(1, len(myList)):
    print(myList)
    itemInsert = myList[index]
    position = index
    while position > 0 and myList[position-1] > itemInsert:
        myList[position] = myList[position-1]
        position -=1
    myList[position] = itemInsert
print(myList)