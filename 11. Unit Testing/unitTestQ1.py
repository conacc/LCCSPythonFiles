# unitTestQ1.py
# @coneill 02/11/2021
# Unit test of a multiplier

# Function to be tested
def multiplier(x,y):
    answer = x*y
    return answer

# Unit test function
def unitTest():
    # Create test data
    testNum1 = 5
    testNum2 = 6
    # Calculate expected value
    expectedVal = testNum1*testNum2
    # Call function with test data
    testAns = multiplier(testNum1,testNum2)
    # Check test result against expected
    if testAns == expectedVal:
        passed = True
    else:
        passed = False
    return passed

# Run the test
print('Test passed: ',unitTest())
        
        
    
    
    
    



