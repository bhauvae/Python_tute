from pandas import DataFrame, Series
import pandas as pd
import numpy as np

data = np.random.randn(50, 3)
for i in range(15):
    data[np.random.randint(0, 50)][np.random.randint(0, 3)] = np.nan
print(data)
frame = DataFrame(data)
to_drop = (frame.isnull().sum(axis=0) > 5)

print(frame.drop(to_drop[to_drop].index, axis=1))
print(frame.drop((frame.sum(axis=1)).idxmax(), axis=0))
print(frame.sort_values(by=0, ascending=False))
