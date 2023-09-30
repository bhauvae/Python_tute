from pandas import DataFrame, Series
import numpy as np

frame = DataFrame(np.arange(1, 101).reshape(10, 10), index=[list('xxxxyyyyzz'),list('aabbccddee'), list('0123456789')])
frame.index.names = ["L1","L2","L3",]
print(frame.loc[('x', 'a', '1')])