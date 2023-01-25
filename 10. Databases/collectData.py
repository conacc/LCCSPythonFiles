# collectData.py
name = "John"
age = 16

import csv
record = [name,age]
file = open("results.csv","a",newline="")
r = csv.writer(file)
r.writerow(record)
file.close()
print("New Record added to CSV")
