import numpy as np

arr = np.arange(1, 101).reshape(10, 10).T
cond = np.array([0, 1, 2, 3, 4])
arr2 = np.arange(1, 126).reshape(5, 5, 5)
arr[:] = 10
arr5 = np.arange(1, 28).reshape(3, 3,3)
arr4 = np.sqrt(arr2)
print(np.where(np.sqrt(arr2) > 8, 0, arr2))
print(arr2[[1,2,3]])
print(arr5)

print(arr5.sum(axis=0))




