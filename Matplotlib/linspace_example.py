import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1,10,10)
y = x * x

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,y,color="b",lw=1,alpha=0.5,linestyle='-',marker='x',markersize=10,markerfacecolor="g",markeredgecolor="r",markeredgewidth=4)
# axes.set_xlim(1,5)
# axes.set_ylim(1,5)
plt.show()


