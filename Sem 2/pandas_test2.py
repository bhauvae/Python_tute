import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
count = [i for c in np.bincount(iris.target) for i in range(1, c + 1)]
index = [iris.target_names[iris.target], count]
data = pd.DataFrame(iris.data, columns=iris.feature_names, index=index)
data.describe()
print(data)
data.corr()