# pandasCSVToLists.py
# Converts a two-column CSV file to two lists

# importing module
from pandas import *

# reading CSV file
data = read_csv("results.csv")
 
# converting column data to list
name = data["name"].tolist()
age = data["age"].tolist()
 
# printing list data
print('Name:', name)
print('Age:', age)