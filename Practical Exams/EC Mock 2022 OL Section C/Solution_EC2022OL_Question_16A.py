# Question 16(a) Solution
# Student name: C O'Neill

# part (i)
print("This program can find the perimeter or area of a quadrilateral")

length = 6
width = 4

# part (ii)
name = input("Please enter your user name: ")

choice = input("Do you want to find the (p)erimeter or (a)rea? ")

# part (iii)
length = input("Please enter the length: ")
length = float(length)
width = input("Please enter the width: ")
width = float(width)

if choice == "p":
    # perim = length + length + width + width
    perim = (2*length) + (2*width) # part (vi)
    perim = round(perim,2) # part (iv)
    print("A quadrilateral of length",length, "and width",width, "has a perimeter of: ",perim) # part (v)
elif choice == "a":
    print("A quadrilateral of length",length, "and width",width, "has an area of: ",round(length*width,2)) # part (iv)
# part (ii)
print("Thank you for using the program",name)