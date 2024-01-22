# menuWithWhileLoop.py
# @coneill 22/01/2024
print("*"*20)
print("1) Area of Circle")
print("2) Volume of Sphere")
print("3) Exit")
print("*"*20)
option = input("Enter option(1-3): ")

while option != "3":   # != not equal to
    if option == "1":
        radius = input("Enter radius: ")
        radius = float(radius) # decimal
        area = 3.14*(radius**2) # power of
        print("Area: ", area)
        option = 0
    elif option == "2":
        radius = input("Enter radius: ")
        radius = float(radius)
        volume = (4/3)*3.14*(radius**3)
        print("Volume: ", volume)
        option = 0
    else:
        print("Invalid entry")    
    print("*"*20)
    print("1) Area of Circle")
    print("2) Volume of Sphere")
    print("3) Exit")
    print("*"*20)
    option = input("Enter option(1-3): ")
print("Thank you and Goodbye")
    
    
    
    
