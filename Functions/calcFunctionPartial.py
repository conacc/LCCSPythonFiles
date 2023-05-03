# calcFunction.py
# @coneill 03/05/2023

# Define Functions
def menu():
    print("Welcome to the calculator.")
    print("1. Square a number")
    print("2. Add two numbers")
    print("3. Multiply two numbers")
    print("4. Odd or Even")
    choice = input("Choose an Option: ")
    choice = int(choice) # cast String to int
    return choice

def squarer(num):
    answer = num**2 # two stars for 'to the power of'
    print("The square of your number is: ",answer)
    
def adder(num1, num2):
    answer = num1+num2 # two stars for 'to the power of'
    print("The sum of your numbers is: ",answer)

def multiplier(num1, num2):
    answer = num1*num2 # two stars for 'to the power of'
    print("The product of your numbers is: ",answer)

# Call Functions
option = menu()

if option == 1:
    userNum = input("Enter a number to square: ")
    userNum = int(userNum) # cast String to int
    squarer(userNum) # call function with argument userNum
elif option == 2:
    print("Enter two numbers to add: ")
    userNum1 = input("First number: ")
    userNum1 = int(userNum1)
    userNum2 = input("Second number: ")
    userNum2 = int(userNum2)
    adder(userNum1, userNum2)
elif option == 3:
    print("Enter two numbers to multiply: ")
    userNum1 = input("First number: ")
    userNum1 = int(userNum1)
    userNum2 = input("Second number: ")
    userNum2 = int(userNum2)
    multiplier(userNum1, userNum2)
