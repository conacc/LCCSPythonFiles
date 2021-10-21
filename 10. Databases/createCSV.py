# createCSV.py
# @coneill 21/10/2021
# Create a new CSV file using python
import csv
header=["make","model","year"]
file=open("cars.csv","a",newline="")
db=csv.writer(file)
db.writerow(header)
file.close()