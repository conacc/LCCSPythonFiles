# unitTestSample.py
# @coneill 02/11/2021
# An example Unit Test of a Function

# Define function to be tested
def volCylinder(radius,height):
    volume = 3.14*radius*radius*height
    return volume

# Define Unit Test Function
def unitTest():
    # Create test data
    testR = 7
    testH = 13
    # Calculate expected value
    expectedVal = 3.14*testR*testR*testH
    # Call the function to be tested
    testAns = volCylinder(testR,testH)
    # Compare Test and Expected Values
    if testAns == expectedVal:
        passed = True
    else:
        passed = False
    return passed
# Run the Unit Test
print("Test result: ",unitTest())

        
        
    
    
    
    
    
    
    