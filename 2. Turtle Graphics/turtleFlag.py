# turtleFlag.py
from turtle import *
shape('turtle')
width(50)
penup()
# goto(-250,250)
flagList = ['red','orange','yellow','green','blue','indigo']
for item in flagList:
    color(item)
    pendown()
    forward(500)
    penup()
    right(90)
    forward(50)
    left(90)
    backward(500)
