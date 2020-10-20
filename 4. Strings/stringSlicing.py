# stringSlicing.py
# @coneill 06/10/2020
# Using index values to slice a String
string1 = 'Hello'
print(string1[1]) # prints 'e'
print(string1[0]) # prints 'H'
print(string1[-1]) # prints 'o' (the last char)
# prints from index 1, up to 4 (not including 4)
print(string1[1:4])
string2 = 'Hello World'
print(string2[4:9]) # prints from index 4 to 8
print(string2[:8])