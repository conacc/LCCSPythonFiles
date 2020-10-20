# turtleRandomCircle.py
# @coneill 23/09/2020
# Draw a random size circle
from turtle import *
import random
shape('turtle')
color('#00e600')
size = random.randrange(5,100)
circle(size)
print(size)