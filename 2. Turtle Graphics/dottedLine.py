# dottedLine.py
# @coneill 18/09/2020
# draws a dotted line
from turtle import *

shape('turtle')
color('black')
speed(1)

penup()
backward(175)
pendown()

for i in range(9):
    forward(20)
    penup()
    forward(20)
    pendown()

