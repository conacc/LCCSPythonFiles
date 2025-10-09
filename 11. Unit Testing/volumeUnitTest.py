# volumeUnitTest.py
# @coneill 08/10/2025

# Function to be tested
def volCylinder(r, h):
    volume = 3.14 * r * r * h
    return volume

# Unit Test Function
# To test a function that takes in r and h
# as arguments and returns vol of Cyl
def unitTest():
    # test data for radius and height
    testR = 2 
    testH = 1
    expectedResult = 3.14 * (testR**2) * testH
    testResult = volCylinder(testR, testH)
    if expectedResult == testResult:
        testPassed = True
    else:
        testPassed = False
    return testPassed
# Call Unit Test Function
print("Test Passed:",unitTest())

