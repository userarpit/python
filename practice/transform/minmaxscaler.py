from sklearn.preprocessing import MinMaxScaler
import numpy as np

data = np.array([[10, 20], [30, 40], [50, 60]])

scaler = MinMaxScaler(feature_range=(1,100))

scaler_data = scaler.fit_transform(data)
print(scaler_data)