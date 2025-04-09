# frequencyGraphs.py
# @coneill 08/04/2025
colourList = ["red", "green", "blue", "blue", "blue", "red"]

nameList = []
colourCount = []

for item in colourList:
    if item not in nameList:
        nameList.append(item)

for colour in nameList:
    total = colourList.count(colour)
    colourCount.append(total)
        
print(nameList)
print(colourCount)

# Draw Pie chart (Book p. 87)
