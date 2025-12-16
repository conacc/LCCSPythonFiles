# fifaGraphs.py
# 15/12/2025

# Import CSV Data Set
from pandas import *
data = read_csv("FIFA21-player-list.csv")

# Create lists from Data Set
ageList = data["age"].tolist()
wageList = data["wage_eur"].tolist()
heightList = data["height_cm"].tolist()
weightList = data["weight_kg"].tolist()

# Print Lists
print(ageList)
print(wageList)

# Graph the data from lists
import matplotlib.pyplot as plt
plt.scatter(ageList,wageList)
plt.title("Player Wages, shown by age")
plt.xlabel("Age (years)")
plt.ylabel("Wages(€)")
plt.show()

plt.scatter(heightList,weightList)
plt.title("Player Height and Weight")
plt.xlabel("Height(cm)")
plt.ylabel("Weight(kg)")
plt.show()

# Univariate graph
plt.hist(ageList) # Histogram
plt.xlabel("Age (years)")
plt.ylabel("Frequency")
plt.show()


