# pandasColumnstoRows.py
# Converts a two-column CSV file to two lists

# importing module
from pandas import *

file = read_csv("results.csv")
# adding header
headerList = ['age1', 'age2']
  
# converting data frame to csv
file.to_csv("results.csv", header=headerList, index=False)


# reading CSV file
data = read_csv("results.csv")
 
# converting column data to list
age1 = data["age1"].tolist()
age2 = data["age2"].tolist()
 
# printing list data
print('Age1:', age1)
print('Age2:', age2)