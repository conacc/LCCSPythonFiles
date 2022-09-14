# mathsFunctions.py
# @coneill 08/09/2022
'''
a = 4
answer = a*2
print(answer)
'''
# Define function
def doubler(num):
    answer = num*2
    return answer

def trebler(num):
    answer = num*3
    return answer

def adder(num1,num2):
    answer = num1+num2
    return answer

# Call function
output = doubler(16)
print(output)
output = trebler(76)
print(output)
output = adder(13,19)
print(output)


