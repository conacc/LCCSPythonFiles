# fifaPandas.py
# @coneill 05/04/2022
# Pandas Analytics Module Tutorial
import pandas

# Read in CSV file as Pandas DataFrame
fifaDF=pandas.read_csv('FIFA21-player-list.csv')

# Print number of rows
print('Rows: ',len(fifaDF))

# Print rows and columns
print('Shape(rows,cols):', fifaDF.shape)

# Create new DF with three columns
nameAgeValueDF=fifaDF[['short_name','age','value_eur']]
print(nameAgeValueDF)

irishPlayersDF=fifaDF[fifaDF['nationality']=='Republic of Ireland']
print(irishPlayersDF)

under30DF=fifaDF[fifaDF['age']<30]
print(under30DF)









