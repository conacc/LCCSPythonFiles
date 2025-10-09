# multiplyUnitTest.py
# @coneill 09/10/2025
# Write a Unit Test function for this multiply function

# Function to test
def multiply(a,b):
    product = a**b
    return multiply

# Unit Test
def unitTest():
    testA = 5 
    testB = 6
    expectedResult = testA*testB
    testResult = multiply(testA, testB)
    if expectedResult == testResult:
        testPassed = True
    else:
        testPassed = False
    return testPassed

# Call Unit Test Function
print("Test Passed:",unitTest())
