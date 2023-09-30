import pandas as pd
obj = pd.Series(range(3),index=['a','b','c'])
index=obj.index
index[1]='d'
# TypeError: Index does not support mutable operations