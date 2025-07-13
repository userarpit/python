import sys
print("Python executable:", sys.executable)
print("Python version:", sys.version)

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats



x_actual = np.array([150, 155, 160, 157, 162, 164, 168, 170, 140, 145, 175, 178, 180])
x = x_actual.reshape((-1, 1))
y = np.array([50, 52, 54, 58, 62, 64, 66, 68, 45, 47, 70, 72, 73])

model = LinearRegression().fit(x, y)

print("Intercept : ", model.intercept_)
print("Coefficient:", model.coef_)
print(model.predict(x))
print("*******" * 10)
plt.scatter(x, y)
plt.plot(x, model.predict(x))
plt.show()
print("Initial", model.score(x, y))
print("Enter 0 to exit")
new_number = int(input("Enter the number : "))
while new_number != 0:
    y_predict = model.predict([[new_number]])
    print("before", model.score(x, y))

    x = np.append(x, [[new_number]]).reshape((-1, 1))
    y = np.append(y, y_predict)
    model.fit(x, y)

    print("After", model.score(x, y))
    new_number = int(input("Enter the number : "))

print("Model is {0} accurate".format(model.score(x, y)))
print(model.predict([[151]]))

slope, intercept, r, p, std_err = stats.linregress(x_actual, y)
print("slope : ", slope)
print("intercept : ", intercept)
print("r : ", r)
print("p : ", p)
print("std_err : ", std_err)
