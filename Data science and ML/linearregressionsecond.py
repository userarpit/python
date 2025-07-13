import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv("cars.csv")

# print(df.head())
# print(df.describe())
# x = df[['hp','wt']] # independent variable
# y = df['carb'] # dependent variable
# print(x)
# x.hist()
# plt.show()
# print(x.hp)

print(len(df))
msk = np.random.rand(len(df)) < 0.8

print(msk)
train = df[msk]
print(train)
test = df[~msk]
print(test)
print(test.index)   

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
# print(train[['hp']])
x_train = np.asanyarray(train[['hp']])
y_train = np.asanyarray(train[['carb']])
x_test = np.asanyarray(test[['hp']])
y_test = np.asanyarray(test[['carb']])
print(x_train)
print(y_train)
print(x_test)
print(y_test)

model = LinearRegression().fit(x_train,y_train)

print("Intercept : ",model.intercept_)
print("Coefficient:",model.coef_)

plt.scatter(train.hp,train.carb,color = 'blue')
plt.plot(x_train,model.coef_[0][0] * x_train + model.intercept_[0],'-r')
plt.show()

y_predict = model.predict(x_test)
print(y_predict)

df1 = pd.DataFrame({'Actual': y_test.flatten(),'Predicted':y_predict.flatten()})
print(df1)
df1.plot(kind='bar',figsize=(16,10))
plt.show()

print(metrics.r2_score(y_predict,y_test))