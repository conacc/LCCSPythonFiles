# FifaAnalysis.py
# @coneill 01/03/2023
# Data Analysis Steps:
# 1. Access, 2. Pre-process, 
# 3. Analyse, 4. Visualise

# 1. Access
from pandas import *
dataIn = read_csv("FIFA21-player-list.csv")
#print(dataIn)

ageList = dataIn["age"].tolist()
print(ageList)

# 2. Pre-process data
# No cleaning needed - all ages are valid

# 3. Analyse data
import statistics
print("Mean age: ",statistics.mean(ageList))
print("Modal age: ",statistics.mode(ageList))
print("Median age: ",statistics.median(ageList))
print("Range of ages: ",statistics.variance(ageList))

# 4. Visualise Data
import matplotlib.pyplot as plt
ageList.sort()
plt.plot(ageList)
plt.show()

