# %%
import pandas as pd


data = pd.read_csv('Q9_test data.csv')

# %%
# a) Detect missing values, display TRUE or FALSE
data.isna()

# b) Identify the column(s) which have at least one missing value
sum_col = data.isna().sum()
col = sum_col[sum_col > 0]

# c) Count the number of missing values in each column
data.isna().sum()

# d) Drop the rows where at least one element is missing
sum_row = data.isna().sum(axis=1)
drop_row = sum_row[sum_row > 0]
data.drop(drop_row, axis=0)
# %%
# e) Drop the rows where all elements are missing
data.dropna(axis=0, how="all")
data[data.isnull().any(axis=1)]
# %%
# f) To keep the rows with at least 2 NaN values
drp_row = sum_row[sum_row < 2]
data.drop(drp_row, axis=0)

# g) Total number of missing values
data.isna().sum().sum()

#  h) To replace NaNs with a single constant value in specified columns
data.fillna(data.iloc[0])

# i)  To replace  NaNs  with the value from the previous row or the next row in a given DataFrame
data.fillna(axis=0, method='ffill')

# j) To replace NaNs with median or mean of the specified columns in a given DataFrame.
data['ord_no'].fillna(data['ord_no'].mean())
