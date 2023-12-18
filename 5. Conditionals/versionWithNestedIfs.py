# versionWithNestedIfs.py
# @coneill 18/12/2023
choice = input("Would you like to add (W)ords or (N)umbers?")
choice = choice.upper()

if choice == "N":
    num1 = input("Enter first number: ")
    num1 = int(num1) # cast to integer
    num2 = input("Enter second number: ")
    num2 = int(num2)
    print("Numbers added", num1+num2)
    if (num1+num2) % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")
    
elif choice == "W":
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    print("Words added", word1+word2)
    if (word1+word2).count("e") > 0 or (word1+word2).count("E") > 0:
        print("This word contains an e")
    else:
        print("This word does not contain an e")

else:
    print("That is not a valid entry")
