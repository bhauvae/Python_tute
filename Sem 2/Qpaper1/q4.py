import pandas as pd
import numpy as np

series = pd.Series(np.arange(10))
print(series[series > 6])
