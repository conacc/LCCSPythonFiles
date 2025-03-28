# quickSort.py
# @coneill 12/10/2021
# Sort a list using Quicksort
myList = [85,24,63,45,17,31,96,50]

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
print(quickSort(myList))