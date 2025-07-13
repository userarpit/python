import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([5, 7, 8, 10])
y_points = np.array([25, 49, 64, 100])

plt.scatter(x_points, y_points, s=100, color="red", alpha=0.5, marker="o")
colors = np.array([10, 20, 30, 40])
sizes = np.array([10, 20, 30, 40])
x_points = np.array([1, 2, 3, 6])
y_points = np.array([1, 4, 9, 36])
plt.scatter(x_points, y_points, s=sizes, c=colors, alpha=0.5, marker="s",cmap='prism')

plt.title("Scatter Plot Example")
plt.colorbar()


plt.show()
