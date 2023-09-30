# Load Titanic data from sklearn library , plot the following with proper legend and axis labels:
# a. Plot bar chart to show the frequency of survivors and non-survivors for male and female passengers separately
# b. Draw a scatter plot for any two selected features
# c. Compare density distribution for features age and passenger fare
# d. Use a pair plot to show pairwise bivariate distribution
#  give attention to khwahish
# 4. Using Titanic dataset, do the following
# a. Find total number of passengers with age less than 30
# b. Find total fare paid by passengers of first class
# c. Compare number of survivors of each passenger class
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")

# %%
df["age"].map(lambda x: 1 if x <= 30 else 0).sum()
df['age'][df['age']<=30].count()
# %%

df["fare"].sum()

# %%

df["class"].value_counts()

# %%
sns.scatterplot(x=df["age"], y=df["fare"])

# %%
(df.groupby("class"))["survived"].sum()

# %%
sns.barplot(
    x=((df.groupby("sex"))["survived"].sum()).values,
    y=((df.groupby("sex"))["survived"].sum()).index,
).set(xlabel="survivor")
# %%

plt.plot(x=df["fare"])


# %%
sns.pairplot(df)

# %%
sns.distplot(df['age'])
sns.distplot(df["fare"])
# %%
