# versionWithoutNestedIfs.py
# @coneill 18/12/2023
num1 = input("Enter first number: ")
num1 = int(num1)
num2 = input("Enter second number: ")
num2 = int(num2)
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

choice = input("Would you like to add (W)ords or (N)umbers?")
choice = choice.upper()

if choice == "N":
    print("Numbers added", num1+num2)
    
elif payType == "W":
    print("Words added", word1+word2)

else:
    print("That is not a valid entry")