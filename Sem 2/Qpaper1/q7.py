import pandas as pd
import numpy as np
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([2, 4, 6, 8, 10])

print(np.setdiff1d(ser1, ser2))