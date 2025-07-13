from matplotlib import pyplot as plt
import numpy as np

days = np.arange(0, 21)
other_site, real_python = days, days ** 2

plt.plot(days, other_site)
plt.plot(days, real_python)
plt.xticks([0,5,10,15,20])
plt.xlabel("Days of Reading")
plt.ylabel("Amount of Python learned")
plt.title("Python learned reading Real Python vs Other site")
plt.legend(["Other site", "Real Python"])
plt.show()