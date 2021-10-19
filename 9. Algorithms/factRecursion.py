# factRecursion.py
# @coneill 14/10/2021
# Example of recursion using
# the factorial function

# Define function
def fact(numIn):
    if numIn > 1:
        return numIn*fact(numIn-1)
    else:
        return 1
    
# Call function
answer = fact(5)
print(answer)
    