import pandas as pd
import numpy as np

data = np.random.randint(0, 100, 20)

bin = [0, 18, 25, 35, 60, 100]
cat = pd.cut(data, bin,labels=['A', 'B', 'C', 'D', 'E'])
print(cat)
print(cat.value_counts())
