# volProgramToTestV1.py
# @coneill 19/01/2026
import math
# Function to test
def volSphere(r):
    vol = 4*(math.pi)*r*2
    return vol

# Testing inputs
r = float(input("Enter radius of sphere (metres): "))
answer = volSphere(r)
roundedAns = round(answer,2)
print("Volume is ",roundedAns,"sq metres")