# slicingStrings.py
# @coneill 07/10/2020
# Use string index numbers to slice strings
string1 = 'Hello World'
string2 = 'Goodbye, have a nice day'
# Print the character in index position 1
print(string1[1]) # prints 'e'
print(string2[1]) # prints 'o'
# Print a slice of a string
print(string1[2:8]) # prints from index 2 to 7 (not 8)
print(string2[17:]) # prints from index 17 to end
print(string2[:7]) # prints from start to index 6
print(string1[-1]) # prints final character of string
