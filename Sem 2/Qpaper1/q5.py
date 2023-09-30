import pandas as pd

series = pd.Series([0,1,2,3])
series.reindex([1,0,3,2])
