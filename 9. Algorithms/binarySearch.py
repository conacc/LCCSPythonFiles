# binarysearch.py
# @coneill 18/09/2023
myList = [80,40,30,90,100,20,50]

def binarySearchFn(listIn, key):
    print("List: ",listIn)
    listIn.sort()
    print("Sorted List: ",listIn)
    first = 0
    last = len(listIn) - 1
    while (last-first) >= 0:
        middle = first + ((last - first) // 2)
        if listIn[middle] == key:
            return middle
        elif key < listIn[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return -1

print(binarySearchFn(myList, 90))