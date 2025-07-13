import matplotlib.pyplot as plt

list1 = [23,25,26,27,35,36,38,40,41]


plt.boxplot(list1,vert=False)
plt.grid()
plt.savefig("box.png")
plt.show()