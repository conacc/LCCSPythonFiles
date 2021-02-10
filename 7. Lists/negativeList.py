# negativeList.py
# @coneill 10/02/2021
# Use a for loop to eliminate negatives from a list

ageList = [15, 40, 25, 12, -3, 18, -99]
print(ageList)
# ageList.sort()
# print(ageList)

for i in range(len(ageList)):
    if ageList[i] < 0:
        ageList[i] = 0
print(ageList)