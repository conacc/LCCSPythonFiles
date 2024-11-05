# unitTestExample1.py
# @coneill 05/11/2024

# 1. Define Function to be tested
def largestNum(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
# 2. Define Unit Test Function
def unitTestFn():
    # test cases
    smallNumList = [2, 1, -1, 5, 7]
    bigNumList = [5, 8, 100, 27, 55]
    fails = 0
    for i in range(len(smallNumList)):
        smallNum = smallNumList[i]
        bigNum = bigNumList[i]
        testAns = largestNum(smallNum,bigNum)
        if testAns == bigNum:
            testPass = True
        else:
            testPass = False
            fails += 1
    return testPass, fails
# 3. Call Unit Test Function
print("Results - (Pass,Num Fails):", unitTestFn())

