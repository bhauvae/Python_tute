import numpy as np

array_size = 25


array = np.random.rand(array_size)
array[np.random.choice(array_size, size=int(array_size / 2))] = 0.0
array[np.random.choice(array_size, size=int(array_size / 2))] = np.nan

is_zero = np.where(array == 0)[0]
is_nonzero = np.where(array != 0)[0]
is_nan = np.where(np.isnan(array))[0]

print(array)

print("Indices of zero elements:", is_zero)
print("Indices of non-zero elements:", is_nonzero)
print("Indices of NaN elements:", is_nan)