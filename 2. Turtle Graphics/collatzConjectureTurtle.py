# collatzConjectureTurtle.py
# @coneill 17/10/2022
from turtle import *
shape("turtle")
penup()
goto(-300,300)
pendown()
right(90)
num = input('Enter start number: ')
num = int(num)
counter = 0
while num > 1:
    counter = counter + 1
    if num%2 == 0: # num is even
        forward(50)
        num = num//2
        print(num)
    else: # num is odd
        left(135)
        forward(50)
        right(135)
        num = 3*num+1
        print(num)
print('Your num took this many steps:',counter)
