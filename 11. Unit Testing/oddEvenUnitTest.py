# oddEvenUnitTest.py
# @coneill 09/10/2025

# Function to be tested
def oddEven(num):
    if num // 2 == 0:
        return "even"
    else:
        return "odd"
# Unit Test function
def unitTest():
    testValues = [2,3,4,5,6,9,10]
    fails = 0
    for item in testValues:
        testNum = item 
        if testNum % 2 == 0:
            expectedResult = "even"
        else:
            expectedResult = "odd"
            
        testResult = oddEven(testNum)
        if expectedResult == testResult:
            pass
        else:
            fails += 1
    return fails

# Call Unit Test Function
print("Test Fails:",unitTest())

