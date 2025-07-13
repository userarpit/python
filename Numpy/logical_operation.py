import numpy as np

x = np.arange(5)
print(x)
print(np.logical_and(x > 1, x < 4))
print(np.logical_or(x > 1, x < 4))
print(np.logical_not(x < 4))
