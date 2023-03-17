# csvAddData.py
# Creates two headers and add two-record list to CSV

name = "John"
age = 16

import csv
record = [name,age]
file = open("results.csv","a",newline="")
r = csv.writer(file)
r.writerow(record)
file.close()
print("New Record added to CSV")
