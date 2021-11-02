# unitTestExample.py
# @coneill 02/11/2021
# Sample of a unit test

# Function to be tested
def volCylinder(radius,height):
    # volume = pi*r*r*h
    volume = 3.14*radius*radius*height
    return volume

# Unit test function
def unitTest():
    # Create test data
    testR = 2
    testH = 1
    # Calculate expected value
    expectedVal = 3.14*testR*testR*testH
    # Call function with test data
    testAns = volCylinder(testR,testH)
    # Check test result against expected
    if testAns == expectedVal:
        passed = True
    else:
        passed = False
    return passed

# Run the test
print('Test passed: ',unitTest())
        
        
    
    
    
    



