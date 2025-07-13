import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([0, 100, 4, 6])
ypoints = np.array([0, 100, 200, 250])
plt.subplot(1, 2, 1)
plt.title("Matplotlib Test", loc="left")
plt.plot(ypoints, "o-b", ms=20, mec="r", mfc="y", lw="20")

plt.subplot(1, 2, 2)
plt.plot(xpoints, "o-r", ms=20, mec="y", mfc="b", lw="20")

font1 = {"family": "serif", "color": "blue", "size": 20}
font2 = {"family": "serif", "color": "red", "size": 20}
plt.xticks(fontsize=10)
plt.xlabel("X-axis", fontdict=font1)
plt.ylabel("Y-axis", fontdict=font2)
plt.title("Matplotlib Test", loc="left")

plt.grid(axis="both", color="g", linestyle="-", linewidth=1)
plt.legend(["X-axis", "Y-axis"], loc="upper left", fontsize=10)
plt.suptitle("matplotly test 2 figure")
plt.show()
# print(matplotlib.__version__)

# print(type(xpoints))
