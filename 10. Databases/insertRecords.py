# insertRecords.py
# @coneill 21/10/2021
# Add records to CSV Flat File
import csv
record1=["BMW","X5","2016"]
record2=["Tesla","Model X","2021"]
record3=["Citroen","C3","2013"]
file=open("cars.csv","a",newline="")
db=csv.writer(file)
db.writerow(record1)
db.writerow(record2)
db.writerow(record3)
file.close()

