# removingEvens.py
# @coneill 06/01/2026
# Create a list of 10 positive numbers
myList = [1,2,3,4,5,6,7,8,9,10]

oddList = []
# Loop through list to remove negatives
for item in myList:
    print(item)
    if item%2 != 0:
        oddList.append(item)
#print("Final value of item variable",item)
print(myList)
print(oddList)
