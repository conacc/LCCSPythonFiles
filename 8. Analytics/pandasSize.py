# pandasSize.py
# @coneill 18/03/2021
# Use pandas to find the size of a dataframe
import pandas

# Read the entire CSV file into a pandas DataFrame
fifa_df = pandas.read_csv('FIFA21-player-list.csv')

# Display the length of the dataframe
print("Nr. rows", len(fifa_df))

# Display the number of rows and column
print("Shape (rows, cols)", fifa_df.shape)
