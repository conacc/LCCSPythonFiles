# csvColumnToList.py
# @coneill 08/04/2024

# Import Module
from pandas import *

# Open Comma Separated Value File
# File must be saved in same folder as Python File
data = read_csv("FIFA21-player-list.csv")

# Convert CSV Column to Python List
heightList = data["height_cm"].tolist()

# Print List
print(heightList)