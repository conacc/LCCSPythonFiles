# volumeCalculatorV1.py
# @coneill 19/04/2023
# Using functions to find volume of sphere/cylinder

# Define functions
def welcome():
    print("Welcome to the Vol Calc")

def volSphere(radiusIn):
    volume = (4/3)*3.14*radiusIn**3
    volume = round(volume,2)
    print("The volume of the sphere is: ",volume)

def volCylinder(radiusIn,heightIn):
    volume = 3.14*(radiusIn**2)*heightIn
    volume = round(volume,2)
    print("The volume of the cylinder is: ",volume)
# Call functions
welcome()
volSphere(10)
volSphere(25)
volCylinder(10,50)