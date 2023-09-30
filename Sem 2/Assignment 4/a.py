# $$
import pandas as pd

df1 = pd.read_excel(r"C:\Users\Bhavya\CODE BASE\Python Projects\Python_class\Sem 2\Assignment 4\att1.xlsx")
df2 = pd.read_excel(r"C:\Users\Bhavya\CODE BASE\Python Projects\Python_class\Sem 2\Assignment 4\att2.xlsx")

merge_inner = pd.merge(df1, df2, on='Name', suffixes=('_workshop1', '_workshop2'))

merge_outer = pd.merge(df1, df2, on='Name', how='outer', suffixes=('_workshop1', '_workshop2'))
attended_single_workshop = merge_outer[merge_outer['Date_workshop1'].isnull() | merge_outer['Date_workshop2'].isnull()]

merged_df = pd.concat([df1, df2], ignore_index=True)
total_records = len(merged_df)

merged_df2 = pd.concat([df1, df2], ignore_index=True)
merged_df2.set_index(['Name', 'Date'], inplace=True)
merged_df2.groupby('Name').describe()


# $$
