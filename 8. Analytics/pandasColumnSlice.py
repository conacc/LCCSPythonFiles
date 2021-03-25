# pandasColumnSlice.py
# @coneill 18/03/2021
import pandas
# Slice columns out of a dataframe
fifa_df = pandas.read_csv('FIFA21-player-list.csv')
# Select a number of columns - all rows
fifa_df1 = fifa_df[['short_name', 'age', 'value_eur']]
print(fifa_df1)
