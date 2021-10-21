# userInputRecord.py
# @coneill 21/10/2021
# Adds user's record to Flat file
import csv
# Create user record
newMake=input("Enter make of car: ")
newModel=input("Enter model of car: ")
newYear=input("Enter year of car: ")
newRecord=[newMake,newModel,newYear]
# Add record to CSV file
file=open("cars.csv","a",newline="")
db=csv.writer(file)
db.writerow(newRecord)
file.close()
# Print out full CSV file
file=open("cars.csv","r",newline="")
records=list(csv.reader(file))
file.close()
for record in records:
    print(record)