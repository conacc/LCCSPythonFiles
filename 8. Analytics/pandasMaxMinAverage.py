# pandasMaxMinAverage.py
# @coneill 18/03/2021
import pandas
# Slice columns out of a dataframe
fifa_df = pandas.read_csv('FIFA21-player-list.csv')
# What is the average player age?
print("Average player age:", fifa_df['age'].mean())
# What are the youngest and oldest ages
print("Youngest:", fifa_df['age'].min())
print("Oldest:", fifa_df['age'].max())
# What is the median age and wage of a player?
print("Median age/wage:\n", fifa_df[['age', 'wage_eur']].median())