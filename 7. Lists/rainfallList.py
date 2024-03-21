# rainfallList.py
# @coneill 21/03/2024
# 1. Set up an empty list
rainList = []
# 2. Ask user to input 7 rain values
# and add to list
for i in range(7):
    rainNum = input("Enter today's rain (cm):")
    rainNum = int(rainNum)
    rainList.append(rainNum)
# 3. Print List
print(rainList)
# 4. Calculate total and average rainfall
total = 0
for item in rainList:
    total = total + item
print("Total:",total)
mean = total/len(rainList)
print("Average:",mean)