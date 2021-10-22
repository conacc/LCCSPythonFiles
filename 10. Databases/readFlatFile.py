# readFlatFile.py
# @coneill 21/10/2021
# Read and display Flat File
import csv
file=open("cars.csv","r",newline="")
records=list(csv.reader(file))
file.close()
for record in records:
    print(record)