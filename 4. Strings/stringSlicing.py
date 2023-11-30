# stringSlicing.py
# @coneill 29/11/2023
string1 = "Hello"
string2 = "World"
string3 = string1 + " " + string2 # concatination
print(string1)
print(string2)
print(string3)
print(string1[0])# First Letter (H)
print(string2[3])# Letter in Index 3 (l)
print(string3[5])# Letter in Index 5 (Space)

# Slicing more than one letter from a String
print(string1[2:]) # From index 2 to end
print(string3[3:])
print(string2[:3])# From start to 3 (not including 3)
print(string3[1:8])# From 1 up to 8 (not including 8)

# Multiply Strings
print(string1*3)
print("*"*50)



