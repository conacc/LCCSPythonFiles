# fifaAnalysis.py
# @coneill 11/12/2025

# Import Pandas Module
from pandas import *

# Open CSV File to be Analysed
data = read_csv("FIFA21-player-list.csv")

# Convert CSV column to a python list
ageList = data["age"].tolist()

# Print List and length
print(ageList)
print(len(ageList))

# Built-in Python Statistics Methods
print("Maximum age:",max(ageList))
print("Minimum age:",min(ageList))

# Python Statistics Module Methods
import statistics
print("Mean age:",statistics.mean(ageList))
print("Median age:",statistics.median(ageList))
print("Modal age:",statistics.mode(ageList))

# Graph ages
import matplotlib.pyplot as plt
plt.hist(ageList)
plt.show()


