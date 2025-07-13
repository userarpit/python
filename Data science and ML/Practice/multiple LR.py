import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Generate independent variables
engine_size = (
    np.random.rand(100, 1) * 3.0 + 1.0
)  # Engine sizes between 1.0 and 4.0 liters
horsepower = np.random.rand(100, 1) * 150 + 80  # Horsepower between 80 and 230 HP
# print(engine_size)
# print(horsepower)
# Generate dependent variable (Car Price) with some noise
# Price = 15000 * Engine Size + 100 * Horsepower + 5000 (base price) + random noise
car_price = (
    15000 * engine_size + 100 * horsepower + 5000 + np.random.randn(100, 1) * 5000
)

X = np.hstack((engine_size, horsepower))
# print(X)
y = car_price

df = pd.DataFrame(X, columns=["Engine_size", "Horsepower"])
df["car_price"] = y

print(df.head())

X_train, X_test, y_train, y_test = train_test_split(
    df[["Engine_size", "Horsepower"]], df["car_price"], test_size=0.2, random_state=42
)

# print(X_train)
# print(y_train)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# mse
mse = mean_squared_error(y_test, y_pred)
# r2
r2=r2_score(y_test, y_pred)

print(model.coef_)
print(model.intercept_)
print(mse)
print(r2)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of actual data
ax.scatter(
    X_test["Engine_size"], 
    X_test["Horsepower"], 
    y_test, 
    color='blue', 
    label='Actual Prices'
)

# Create a meshgrid for surface plot
engine_size_range = np.linspace(X_test["Engine_size"].min(), X_test["Engine_size"].max(), 20)
horsepower_range = np.linspace(X_test["Horsepower"].min(), X_test["Horsepower"].max(), 20)
engine_size_grid, horsepower_grid = np.meshgrid(engine_size_range, horsepower_range)
X_grid = np.c_[engine_size_grid.ravel(), horsepower_grid.ravel()]
y_grid_pred = model.predict(X_grid).reshape(engine_size_grid.shape)

# Plot regression surface
ax.plot_surface(
    engine_size_grid, 
    horsepower_grid, 
    y_grid_pred, 
    color='red', 
    alpha=0.5, 
    label='Regression Surface'
)

ax.set_xlabel('Engine Size')
ax.set_ylabel('Horsepower')
ax.set_zlabel('Car Price')
ax.set_title('3D Plot: Engine Size, Horsepower vs Car Price')
plt.legend()
plt.show()

print(model.predict(np.array([[3.863864, 169.971953]])))