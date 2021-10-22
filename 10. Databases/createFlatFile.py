# createFlatFile.py
# @coneill 21/10/2021
# Create flat file database
import csv
header=["make","model","year"]
file=open("cars.csv","a",newline="")
db=csv.writer(file)
db.writerow(header)
file.close()