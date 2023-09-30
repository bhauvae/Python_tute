# &&
import pandas as pd
import numpy as np

# 1 a
ser = pd.Series(np.random.randint(1, 10, 6), index=list('bcdfea'))
ser.sort_values()
ser.sort_index()

# 1 b
ser2 = pd.Series(np.random.randint(1, 10, 40))
ser2.rank(method='first')
ser2.rank(method='max')

# 1 c
ser2.idxmax()
ser2.idxmin()
# &&