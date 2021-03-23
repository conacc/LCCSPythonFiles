# pandasGroupPlot.py
# @coneill 19/03/2021
# Use pandas and matpoltlib to graph
import pandas
from matplotlib import pyplot

# Read in full CSV file as dataframe
fifa_df = pandas.read_csv('FIFA21-player-list.csv')

# Create group with two variables
fifa_df1 = fifa_df[['age', 'wage_eur']]

# Group by age and mean wage and plot
df = fifa_df1.groupby('age')['wage_eur'].mean()
print(df)
pyplot.plot(df)
pyplot.show()