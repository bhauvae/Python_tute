from pandas import DataFrame
import numpy as np


data = {'a': [1, 2, 3], 'b': [2, 3, 4]}
x2 = DataFrame(data, columns=['a', 'b', 'c'])
print(x2)
