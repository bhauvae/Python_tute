import numpy as np

a = np.random.randint(0, 20, size=[10, 4])

a.mean(axis=1)
a.std(axis=1)

type(a)
a.reshape(4, 10)
b = np.random.randint(0, 20, 10)
b
b[:].dtype
ar1 = np.random.randint(0, 10, 10)
ar2 = np.random.randint(0, 10, 10)
ar3 = np.random.randint(0, 10, 10)
ar4 = ar3 - ar2
ar5 = 2 * ar1
np.corrcoef(ar1, ar4)
np.corrcoef(ar1, ar5)
np.cov(ar1, ar4)
np.cov(ar1, ar5)
arr1 = np.random.randint(0, 10, 10)
arr2 = np.random.randint(0, 10, 10)
arr1[0:5] + arr2[0:5]
arr1[5:] * arr2[5:]
arr = np.array([0, 1, 2, np.nan, 0, 3, 4, np.nan])

zero_indices = np.where(arr == 0)[0]
non_zero_indices = np.where(arr != 0)
nan_indices = np.where(np.isnan(arr))
