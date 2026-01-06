# removingNegatives.py
# @coneill 06/01/2026
# Create a list of 10 integers, +ve and -ve
myList = [-5,1,2,3,4,5]
# Print the length, min and max of list
print("Length:",len(myList))
print("Max:",max(myList))
print("Min:",min(myList))
# Add two more numbers and print new list
myList.append(-100)
myList.append(100)
print(myList)
positiveList = []
# Loop through list to remove negatives
for item in myList:
    print(item)
    if item > 0:
        positiveList.append(item)
#print("Final value of item variable",item)
print(myList)
print(positiveList)
