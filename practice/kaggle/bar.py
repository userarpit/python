import matplotlib.pyplot as plt
import numpy as np

x = ["A", "B", "C", "D"]
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color='r', width=0.5)
plt.title("Bar Chart Example", loc="left")
plt.xlabel("Categories")
plt.ylabel("Values")
# plt.barh(x,y,color='red')
plt.show()


