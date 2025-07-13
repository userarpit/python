from matplotlib import pyplot as plt
import numpy as np

xs = list(range(1, 6))
# ys = list(range(2, 11, 2))
ys = [3, -1, 4, 0, 6]
plt.plot(xs, ys, "b--o")
plt.plot([1,2,3,4,5],"g-^")
plt.plot(np.arange(1,21).reshape(5,4))
plt.plot(np.arange(1,21).reshape(5,4).transpose())
plt.show()
