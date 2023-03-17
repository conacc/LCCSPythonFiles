# csvAddData.py
# Creates two headers and add a two-record list to CSV

name = "John"
age = 16

import csv
headerList = ['NAME', 'AGE']

file = open("results.csv","a",newline="")
r = csv.writer(file)
r.writerow(header)
recordList = [name,age]
r.writerow(recordList)
file.close()
print("New Record added to CSV")
