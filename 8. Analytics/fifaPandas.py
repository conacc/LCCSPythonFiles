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

# Create new DF with one type of player
irishPlayersDF=fifaDF[fifaDF['nationality']=='Republic of Ireland']
print(irishPlayersDF)
under30DF=fifaDF[fifaDF['age']<30]
print(under30DF)

# Basic Statistics
print('Youngest player age:',fifaDF['age'].min())
print('Oldest player age:',fifaDF['age'].max())
print('Mean player age:',fifaDF['age'].mean())
print('Median player age:',fifaDF['age'].median())

# Count players by age
ageCount = fifaDF['age'].value_counts()
print(ageCount)
# Count players by Country Represented
countryCount = fifaDF['nationality'].value_counts()
print(countryCount)
# Count players by Club Represented
clubCount = fifaDF['club_name'].value_counts()
print(clubCount)
