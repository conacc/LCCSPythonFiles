# volumeFunctions.py
# @coneill 14/09/2022

#Define function
def volCube(sideIn):
    volume = sideIn*sideIn*sideIn
    return volume

def volSphere(radiusIn):
    volume = (4/3)*(3.14)*(radiusIn**3)
    return volume

def volCylinder(radiusIn,heightIn):
    volume = (3.14)*(radiusIn**2)*(heightIn)
    return volume
# Call functions
print("Volume of Cube")
num = input('Enter side length of cube: ')
num = int(num) # convert input to an integer
output = volCube(num)
print(output)
print("Volume of Sphere")
num = input('Enter radius of sphere: ')
num = int(num) 
output = volSphere(num)
print(output)
print("Volume of Cylinder")
num1 = input('Enter radius of cylinder: ')
num1 = int(num1)
num2 = input('Enter height of cylinder: ')
num2 = int(num2) 
output = volCylinder(num1,num2)
print(output)