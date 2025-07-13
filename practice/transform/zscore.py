import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

array = np.array([10, 12, 14, 16, 18])
print(array)


def zscore(num, array):
    """find zscore and return it"""
    mean = np.mean(array)
    print(mean)
    std_dev = np.std(array)
    print(std_dev)
    z_scores = (num - mean) / std_dev
    return z_scores


print(zscore(16, array))

print("*" * 40)
data = np.array([[10, 20], [30, 40], [50, 60]])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
print(scaler.mean_)
print(scaler.scale_)

    