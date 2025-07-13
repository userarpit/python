import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt

model = LinearRegression()

df = pd.read_csv("cars.csv")

# print(df.head())
# print(df.describe())
x = df[['hp', 'wt']]  # independent variable
y = df['carb']  # dependent variable
print(x)
print(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

model.fit(x_train, y_train)
y_predict = model.predict(x_test)
print(y_predict)

print(np.sqrt(metrics.mean_squared_error(y_test,y_predict)))

plt.bar(range(1,14,2),y_predict, label = "predicted_value")
plt.bar(range(2,15,2),y_test, label = "actual_value", color="r")
plt.legend()
plt.xlabel("bar number")
plt.ylabel("bar hight")
plt.title("Predicted value vs Actual value")
plt.show()

