# pandasCSVToList.py
# Converts a one column CSV file to a list
# The Pandas Package must be installed first

# importing module
from pandas import *

# reading CSV file
data = read_csv("results.csv")

# converting column data to list
soundList = data["sound"].tolist()

# printing list data
print('Sound values:', soundList)
