from sklearn.preprocessing import MaxAbsScaler
import numpy as np

# Sample data (contains zeros)
data = np.array([
    [1.0,  2.0,  0.0],
    [2.0,  0.0, -1.0],
    [0.0,  1.0,  0.5]
])

scaler = MaxAbsScaler()
scaled_data = scaler.fit_transform(data)

print("Original Data:\n", data)
print("\nScaled Data:\n", scaled_data)