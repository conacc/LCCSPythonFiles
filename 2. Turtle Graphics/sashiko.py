# sashiko.py
# @coneill 13/10/2021
# Creates Sashiko Pattern from Binary Numbers

# Define functions
def nameToBinary(name):
    nameList = []
    for i in range(len(name)):
        nameList.append(int(name[i]))
    return nameList
    

def sashikoFirst(myList):  
    for i in range(len(myList)):
        penup()
        goto(-280,280-(size*i))
        if myList[i] == 1:
            for i in range(4):
                pendown()
                forward(size)
                penup()
                forward(size)
        elif myList[i] == 0:
            for i in range(4):
                forward(size)
                pendown()
                forward(size)
                penup()

def sashikoSurname(myList):
    right(90)
    for i in range(len(myList)):
        penup()
        goto(-280+(size*i),280)
        if myList[i] == 1:
            for i in range(4):
                pendown()
                forward(size)
                penup()
                forward(size)
        elif myList[i] == 0:
            for i in range(4):
                forward(size)
                pendown()
                forward(size)
                penup()

def drawSquare():
    goto(-280,280)
    pendown()
    for i in range(4):
        forward(size*8)
        left(90)  
        
# Input Binary Codes for First and Surnames
firstName=input('Please enter the 8-bit Binary for your First Name: ')
secondName=input('Please enter the 8-bit Binary for your Second Name: ')

# Import turtlelibrary
from turtle import *

# Set shape, size and speed parameters
shape('turtle')
speed(9)
size = 70

# Call functions
firstList = nameToBinary(firstName)
surnameList = nameToBinary(secondName)
print('Firstname',firstList)
print('Surname',surnameList)
sashikoFirst(firstList)
sashikoSurname(surnameList)
drawSquare()


    
