import numpy as np
from sklearn.preprocessing import RobustScaler

data = np.array([
    [10, 20],
    [30, 40],
    [50, 60],
    [1000, 2000]  # Outlier
])

scaler = RobustScaler()
scaled_data = scaler.fit_transform(data)

print(data)
print(scaled_data)