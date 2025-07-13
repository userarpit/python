import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import metrics


df = pd.read_csv("cars.csv")

# print(df.head())
# print(df.describe())
x = df[['hp','wt']] # independent variable
y = df['carb'] # dependent variable

model = LinearRegression().fit(x,y)
print(model.predict([[100,2.500]]))

print(model.intercept_)
print(model.coef_)
print(model.predict([[100,3.500]]))
print("*******************")
y_predict = model.predict(x)
print(y)
print(y_predict)

plt.bar(range(1,20,2),y_predict[0:10], label = "predicted_value")
plt.bar(range(2,21,2),y[0:10], label = "actual_value", color="r")
plt.legend()
plt.xlabel("bar number")
plt.ylabel("bar hight")
plt.title("Predicted value vs Actual value")
plt.show()

print(np.sqrt(metrics.mean_squared_error(y,y_predict)))
