# Load a Pandas dataframe with a selected dataset. Identify and count the missing values
# in a dataframe. Clean the data after removing noise as follows
# %%
import pandas as pd
import numpy as np
import seaborn as sns


# a. Drop duplicate rows.
# b. Detect the outliers and remove the rows having outliers
# c. Identify the most correlated positively correlated attributes and negatively correlated attributes

# %%
df = sns.load_dataset('iris')
df.drop_duplicates()
# %%
df.corr()

# %%
outliers_max = df.quantile(q=0.75) + ((df.quantile(q=0.75) - df.quantile(q=0.25)) * 1.5)
outliers_min = df.quantile(q=0.25) - ((df.quantile(q=0.75) - df.quantile(q=0.25)) * 1.5)
outliers = df[(df>=outliers_max) | (df<=outliers_min)]
# %%


