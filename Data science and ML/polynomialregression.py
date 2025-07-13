import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = range(1, 19)  # hours of the day
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]  # speed
plt.scatter(x, y)


mymodel = np.poly1d(np.polyfit(x, y, 3))
myline = np.linspace(1, 18, 100)

plt.plot(myline, mymodel(myline))
plt.show()

print(r2_score(y, mymodel(x)))
print(mymodel(17))
