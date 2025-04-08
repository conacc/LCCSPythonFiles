# fifaGraph.py
# @coneill 07/04/2025

# Import Module
from pandas import *

# Open Comma Separated Value File
# File must be saved in same folder as Python File
data = read_csv("FIFA21-player-list.csv")

# Convert CSV Column to Python List
heightList = data["height_cm"].tolist()
weightList = data["weight_kg"].tolist()

# Print List
print(heightList)
print(weightList)

# Graph height vs weight
import matplotlib.pyplot as plt
plt.scatter(heightList,weightList) # Scatter plot
plt.title("Height and Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.show()




