import numpy as np
arr = np.array([1,3,57,43,6,2223,2])
x = np.searchsorted(arr, [3,6])
print(x)