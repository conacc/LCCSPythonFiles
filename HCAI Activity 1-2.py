import pandas as pd
from matplotlib import pyplot as plt

# we use a built in fuction in pandas to import
url='https://drive.google.com/file/d/1NlWuhV-hctUI8MUW-9aQmx2aJ_LM4ID6/view?usp=drive_link'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
adult_df = pd.read_csv(url)

plt.hist(adult_df["age"])

plt.title("Age of People")
plt.xlabel("Age")
plt.ylabel("Number of people")

plt.show()

plt.scatter(adult_df["gender"], adult_df["occupation"])

ax = plt.gca()
ax.tick_params(axis='x', labelrotation=45)

plt.show()

plt.hist(adult_df["race"])

ax = plt.gca()
ax.tick_params(axis='x', labelrotation=45)

plt.grid(True)

plt.show()

plt.hist(adult_df["native-country"])

ax = plt.gca()
ax.tick_params(axis='x', labelrotation=90)

plt.show()

plt.hist(adult_df["income"])

plt.title("Total amount under 50K and over 50K")
plt.xlabel("under or over 50k")
plt.ylabel("Number of People")


plt.show()