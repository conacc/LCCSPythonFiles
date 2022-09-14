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
output = volCube(5)
print(output)
print("Volume of Sphere")
output = volSphere(5)
print(output)
print("Volume of Cube")
output = volCylinder(5,10)
print(output)