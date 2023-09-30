import numpy as np

arr = np.random.randn(10)

print(arr[:round(0.5*len(arr))])
