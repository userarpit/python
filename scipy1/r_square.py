import numpy as np
from scipy import stats
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

x = 2 * np.random.randn(100, 1)
print(x)
y = 4 + 3 * x + np.random.randn(100, 1)
print(y)

x_flat = x.flatten()
y_flat = y.flatten()

model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

r2_score = r2_score(y, y_pred)

print(r2_score)
