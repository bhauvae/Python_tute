# Import iris data using sklearn library or (Download IRIS data from:
# https://archive.ics.uci.edu/ml/datasets/iris or import it from sklearn.datasets)
# a. Compute mean, mode, median, standard deviation, confidence interval an standard error for each feature
# b. Compute correlation coefficients between each pair of features and plot heatmap
# c. Find covariance between length of sepal and petal
# d. Build contingency table for class feature

# %%
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

df = pd.DataFrame(load_iris().data, columns=load_iris().feature_names)

# %%
df.describe()
# %%
import seaborn as sns
sns.heatmap(df.corr(),cmap="Greys")
# %%
np.cov(df['sepal length (cm)'],df['petal length (cm)'])

# %%
df.cov()

# %%
pd.crosstab(pd.cut(df['sepal length (cm)'],bins=5),columns=pd.cut(df['petal length (cm)'],bins=5))
# %%
