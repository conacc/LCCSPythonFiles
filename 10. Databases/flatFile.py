# flatFile.py
# @coneill 20/10/2021
# Open a CSV Flat File

# 1 Reading a CSV file
file = open("PatientList.csv","r") #read only
data = file.read()
print(data)
file.close()

# Split data after each new line
records = data.split("\n")
# Print table with tabs
print(records[0].replace(",","\t"))
print("-"*40)
for row in records[1:]:
    print(row.replace(",","\t"))

# 2 Amending a CSV file
newFName="Elon"
newLName="Musk"
newDob="01/01/1995"
newPhone="564287"
file=open("PatientList.csv","a") #open to amend
file.write(newFName+','+newLName+','+newDob+','+newPhone+'\n')
file.close()



