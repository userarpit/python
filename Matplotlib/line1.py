import numpy as np
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,20,30,40]
# plt.plot(x,y)
# plt.show()

my_grid = plt.GridSpec(3,3)
my_fig = plt.figure(figsize=(10,10))
my_fig.add_subplot(my_grid[0,:2])
arr = np.arange(1,3,0.2)
plt.plot(arr,':',marker='*',label="line")
plt.grid()
plt.legend(loc="lower right")
plt.savefig("plot.png")

my_fig.add_subplot(my_grid[1,:3])
list1 = [23,25,26,27,35,36,38,40,41]
plt.boxplot(list1,vert=False)
plt.grid()

my_fig.add_subplot(my_grid[0,2])
list1 = [23,25,26,27,35,36,38,40,41]
plt.boxplot(list1,vert=True)
plt.grid()

plt.show()
