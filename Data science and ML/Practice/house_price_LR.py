import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
house_size = np.random.rand(100, 1) * 2000 + 500
# print(house_size)
house_price = 50 * house_size + 50000 + np.random.randn(100, 1) * 10000

X = house_size
y = house_price

# print(type(X))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# print(y_test)
# print(X_test)

model = LinearRegression()
model.fit(X_train, y_train)

print(model.coef_)
print(model.intercept_)

# y pred
y_pred = model.predict(X_test)

# print(y_pred)
# print(y_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# print(mse)
# print(r2)

plt.figure(figsize=(12, 8))

plt.scatter(X_train, y_train, color="blue", label="Training data")
plt.plot(
    X_train,
    model.predict(X_train),
    color="red",
    linewidth=2,
    label="Regression Line (Trained)",
)
plt.grid(True)
plt.legend()
plt.title("Linear Regression")
plt.xlabel("House size")
plt.ylabel("House price")
plt.show()

plt.figure(figsize=(12, 8))

plt.scatter(X_test, y_test, color="blue", label="Testing data")
plt.plot(
    X_test,
    y_pred,
    color="red",
    linewidth=2,
    label="Regression Line (Test)",
)
plt.grid(True)
plt.legend()
plt.title("Linear Regression")
plt.xlabel("House size")
plt.ylabel("House price")
plt.show()

print(model.predict(np.array([[1500]])))
