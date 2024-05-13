# cylSphere.py
# @coneill 09/05/2024
import math
# Define Menu Function
def displayMenu():
    print("*"*30)
    print("Choose from these options:")
    print("1.\t Volume of Sphere")
    print("2.\t Volume of Cylinder")
    print("*"*30)
    choice = input("Enter 1 or 2: ")
    return choice

# Define Sphere Function
def volSphere(r):
    volume = (4/3)*(math.pi)*r**3
    return volume

# Define Cylinder Function
def volCyl(r,h):
    volume = (math.pi)*(r**2)*h
    return volume

# Call Menu function
menuChoice = displayMenu()

if menuChoice == "1":
    print("Volume of Sphere")
    rad = input("Enter the radius in cm:")
    rad = float(rad)
    answer = volSphere(rad)
    print("Vol of Sphere: ",round(answer,2),"cm^3")

elif menuChoice == "2":
    print("Volume of Cylinder")
    rad = input("Enter the radius in cm:")
    rad = float(rad)
    hei = input("Enter the height in cm:")
    hei = float(hei)
    answer = volCyl(rad,hei)
    print("Vol of Cylinder: ",round(answer,2),"cm^3")

else:
    print("Invalid entry")
