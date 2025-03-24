# csvColumnToList.py
# @coneill 24/03/2025

# Import Module
from pandas import *

# Open Comma Separated Value File
# File must be saved in same folder as Python File
data = read_csv("filename.csv")

# Convert CSV Column to Python List
myList = data["column_label"].tolist()

# Print List
print(myList)
