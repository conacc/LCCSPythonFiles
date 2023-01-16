# stringNameExerciseSolution.py
# @coneill 16/01/2023
# A program that asks user to enter their
# name, then tells them how long it is,
# what it starts and ends with, and
# prints it out in all lower and all 
# upper case
name = input("Please enter your name: ")
print("Your name is",len(name),"letters long")
print("The first letter is: "+name[0])
print("The last letter is: "+name[-1])
print("All lower: "+name.lower())
print("All lower: "+name.upper())
