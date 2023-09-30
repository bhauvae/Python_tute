from pandas import DataFrame, Series
import numpy as np

data = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}

df = DataFrame(data)
df['d'] = np.nan
print(df.iloc[1])
index = df.index
print(index.append(index))
print(df)
print(DataFrame(Series([1, 2, 3, 4], index=[0, 4, 8, 12]).reindex(range(12), method='ffill')))
series = Series(df.iloc[1])
print(series)
df2 = (DataFrame(np.arange(25).reshape((5, 5)), columns=list('abcde'), index=list('pqrst')))
print(df2)
print(df2.sum(axis=0))

print(df2.drop('p'))
